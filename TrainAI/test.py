import pygame
import pymunk
import pymunk.pygame_util
import math
import random
import time

# --- การตั้งค่าเบื้องต้น ---
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulation with RL, Penalty & Ball Reset (Stop Condition)")
clock = pygame.time.Clock()

# กำหนดสี
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Arial", 30)

# --- สร้างพื้นที่จำลอง ---
space = pymunk.Space()
space.gravity = (0, 0)  # top-down simulation ไม่ใช้แรงโน้มถ่วง

def create_boundaries(space, width, height):
    static_lines = [
        pymunk.Segment(space.static_body, (0, 0), (width, 0), 5),
        pymunk.Segment(space.static_body, (width, 0), (width, height), 5),
        pymunk.Segment(space.static_body, (width, height), (0, height), 5),
        pymunk.Segment(space.static_body, (0, height), (0, 0), 5)
    ]
    space.add(*static_lines)

create_boundaries(space, width, height)

# --- สร้างวัตถุต่าง ๆ ---
ball_radius = 15  # กำหนดขนาดของบอล

def create_ball(space, pos, radius=ball_radius, mass=1):
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.9
    shape.friction = 0.5
    space.add(body, shape)
    return body

ball = create_ball(space, (width/2, height/2))

def create_robot(space, pos, size=(40, 20), mass=2):
    w, h = size
    moment = pymunk.moment_for_box(mass, size)
    body = pymunk.Body(mass, moment)
    body.position = pos
    body.damping = 0.9  # ลดความเร็วโดยใช้ damping
    shape = pymunk.Poly.create_box(body, size)
    shape.elasticity = 0.5
    shape.friction = 0.5
    space.add(body, shape)
    return body

# --- สร้างทีมหุ่นยนต์ ---
team_A_positions = [(150, 200), (150, 300), (150, 400)]
team_B_positions = [(650, 200), (650, 300), (650, 400)]

team_A = [create_robot(space, pos) for pos in team_A_positions]
team_B = [create_robot(space, pos) for pos in team_B_positions]

draw_options = pymunk.pygame_util.DrawOptions(screen)

# --- กฎการแข่งขัน ---
score_A = 0  # คะแนนทีม A
score_B = 0  # คะแนนทีม B
goal_threshold = 20  # ระยะนับเป็นประตูจากขอบสนาม
goal_height = 200    # ความสูงของเขตประตู (อยู่ตรงกลางแนวตั้ง)

def reset_ball():
    ball.position = (width/2, height/2)
    ball.velocity = (0, 0)

def reset_players():
    for robot, pos in zip(team_A, team_A_positions):
        robot.position = pos
        robot.velocity = (0, 0)
    for robot, pos in zip(team_B, team_B_positions):
        robot.position = pos
        robot.velocity = (0, 0)

def keep_robot_in_bounds(robot, margin_x=20, margin_y=10):
    x, y = robot.position
    new_x = max(margin_x, min(x, width - margin_x))
    new_y = max(margin_y, min(y, height - margin_y))
    if (new_x, new_y) != (x, y):
        robot.position = (new_x, new_y)
        robot.velocity = (0, 0)

# --- Reinforcement Learning Setup ---
def get_state(distance):
    if distance < 50:
        return "close"
    elif distance < 150:
        return "medium"
    else:
        return "far"

def choose_action(q_values, epsilon):
    if random.random() < epsilon:
        return random.choice([0, 1, 2])
    else:
        return q_values.index(max(q_values))

# Hyperparameters สำหรับ Q-learning
alpha = 0.1       # learning rate
gamma = 0.9       # discount factor
epsilon = 0.1     # exploration rate (จะลดลงทุก episode)
min_epsilon = 0.01
epsilon_decay = 0.99
force_step = 200  # ปรับให้ force เปลี่ยนทีละน้อย
initial_force = 2000  # ค่า initial_force ที่ลดลง

# สำหรับหุ่นยนต์แต่ละตัว เก็บค่า force_strength, Q-table และ state
robot_params = {}
for robot in team_A + team_B:
    dx = ball.position.x - robot.position.x
    dy = ball.position.y - robot.position.y
    initial_distance = math.hypot(dx, dy)
    state = get_state(initial_distance)
    q_table = {"close": [0, 0, 0],
               "medium": [0, 0, 0],
               "far": [0, 0, 0]}
    robot_params[robot] = {
        "force_strength": initial_force,
        "prev_distance": initial_distance,
        "state": state,
        "q_table": q_table
    }

def control_robot(robot, force_strength):
    rx, ry = robot.position
    bx, by = ball.position
    vector = (bx - rx, by - ry)
    distance = math.hypot(vector[0], vector[1])
    if distance == 0:
        return
    direction = (vector[0] / distance, vector[1] / distance)
    force = (direction[0] * force_strength, direction[1] * force_strength)
    robot.apply_force_at_local_point(force, (0, 0))

# --- Simulation Loop ---
start_time = time.time()  # เก็บเวลาเริ่มต้น
running = True
episode = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # เงื่อนไขหยุด simulation เมื่อผ่านไป 1 นาที หรือเมื่อทีมใดทีมหนึ่งได้ 5 ประตู
    elapsed_time = time.time() - start_time
    if elapsed_time >= 60 or score_A >= 5 or score_B >= 5:
        print("Stopping simulation...")
        print(f"Final Score - Team A: {score_A}  Team B: {score_B}")
        running = False
        continue

    screen.fill(WHITE)
    
    # ควบคุมหุ่นยนต์ด้วย RL และอัปเดต action
    for robot in team_A + team_B:
        params = robot_params[robot]
        rx, ry = robot.position
        bx, by = ball.position
        current_distance = math.hypot(bx - rx, by - ry)
        current_state = get_state(current_distance)
        q_values = params["q_table"][current_state]
        action = choose_action(q_values, epsilon)
        
        params["prev_state"] = current_state
        params["prev_distance"] = current_distance
        params["action"] = action
        
        # เลือก action: 0 = ลด, 1 = ไม่เปลี่ยน, 2 = เพิ่ม force_strength
        if action == 0:
            params["force_strength"] = max(params["force_strength"] - force_step, 1000)
        elif action == 2:
            params["force_strength"] += force_step
        
        control_robot(robot, params["force_strength"])
    
    dt = 1.0 / 60.0
    space.step(dt)
    
    # อัปเดต RL สำหรับแต่ละหุ่นยนต์ (ปรับ Q-table) พร้อมเพิ่มบทลงโทษ
    for robot in team_A + team_B:
        params = robot_params[robot]
        rx, ry = robot.position
        bx, by = ball.position
        new_distance = math.hypot(bx - rx, by - ry)
        new_state = get_state(new_distance)
        
        # Reward: ให้ reward จากการเข้าใกล้บอล (ลดระยะห่าง)
        # bonus เมื่อเข้าใกล้มาก (new_distance < 30)
        # หากระยะห่างเพิ่มขึ้นมาก (มากกว่า prev_distance + 20) ให้ลงโทษ
        reward = params["prev_distance"] - new_distance
        if new_distance < 30:
            reward += 10
        if new_distance > params["prev_distance"] + 20:
            reward -= 10
        
        old_q = params["q_table"][params["prev_state"]][params["action"]]
        max_future_q = max(params["q_table"][new_state])
        new_q = old_q + alpha * (reward + gamma * max_future_q - old_q)
        params["q_table"][params["prev_state"]][params["action"]] = new_q
        
        params["state"] = new_state
        params["prev_distance"] = new_distance

    # ตรวจสอบประตู
    bx, by = ball.position
    goal_scored = False
    if bx < goal_threshold and (height/2 - goal_height/2 < by < height/2 + goal_height/2):
        score_B += 1
        print(f"Goal for Team B! Score: Team A {score_A} - Team B {score_B}")
        goal_scored = True
    elif bx > width - goal_threshold and (height/2 - goal_height/2 < by < height/2 + goal_height/2):
        score_A += 1
        print(f"Goal for Team A! Score: Team A {score_A} - Team B {score_B}")
        goal_scored = True

    # ตรวจสอบว่าบอลออกนอกสนาม (รวมขนาดของบอล)
    if (ball.position.x < -ball_radius or ball.position.x > width + ball_radius or 
        ball.position.y < -ball_radius or ball.position.y > height + ball_radius):
        print("Ball out of bounds! Resetting ball to center.")
        reset_ball()

    if goal_scored:
        reset_ball()
        reset_players()
        episode += 1
        epsilon = max(min_epsilon, epsilon * epsilon_decay)
        print(f"Episode {episode}: epsilon = {epsilon:.3f}")
        for robot in team_A + team_B:
            rx, ry = robot.position
            dx = ball.position.x - rx
            dy = ball.position.y - ry
            dist = math.hypot(dx, dy)
            robot_params[robot]["prev_distance"] = dist
            robot_params[robot]["state"] = get_state(dist)
        pygame.display.flip()
        time.sleep(1)

    # ตรวจสอบให้หุ่นยนต์ไม่ออกนอกสนาม
    for robot in team_A + team_B:
        keep_robot_in_bounds(robot)

    space.debug_draw(draw_options)
    
    # วาดตำแหน่งของหุ่นยนต์ (จุดสี) สำหรับแต่ละทีม
    for robot in team_A:
        pos = (int(robot.position.x), int(robot.position.y))
        pygame.draw.circle(screen, GREEN, pos, 5)
    for robot in team_B:
        pos = (int(robot.position.x), int(robot.position.y))
        pygame.draw.circle(screen, BLUE, pos, 5)
    
    # วาดกรอบประตู
    left_goal_rect = pygame.Rect(0, height/2 - goal_height/2, goal_threshold, goal_height)
    pygame.draw.rect(screen, RED, left_goal_rect, 2)
    right_goal_rect = pygame.Rect(width - goal_threshold, height/2 - goal_height/2, goal_threshold, goal_height)
    pygame.draw.rect(screen, RED, right_goal_rect, 2)
    
    # แสดงคะแนนและค่า epsilon บนหน้าจอ
    score_text = font.render(f"Team A: {score_A}   Team B: {score_B}", True, BLACK)
    screen.blit(score_text, (width/2 - score_text.get_width()/2, 20))
    epsilon_text = font.render(f"Epsilon: {epsilon:.3f}", True, BLACK)
    screen.blit(epsilon_text, (20, 20))
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
