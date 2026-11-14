from collections import deque

# 1. ENVIRONMENT: A simple map of states an AI Lead-Qualifier Agent can take
# Each state connects to the next possible actions
agent_workflow = {
    "New Lead Received": ["Check Budget", "Send Brochure"],
    "Send Brochure": ["Follow Up Email"],
    "Check Budget": ["High Budget -> Book Call", "Low Budget -> Send Free Guide"],
    "Follow Up Email": ["High Budget -> Book Call"],
    "Send Free Guide": [],
    "High Budget -> Book Call": ["GOAL: Meeting Confirmed"],
    "GOAL: Meeting Confirmed": []
}

# 2. AGENT LOGIC: Breadth-First Search (BFS) from CS50 AI Lecture 0
# Finds the fastest sequence of actions to reach the goal
def find_fastest_action_plan(start_state, goal_state):
    # Queue stores paths we are exploring: [[start_state]]
    queue = deque([[start_state]])
    visited = set()

    while queue:
        # Take the oldest path from the front of the queue
        current_path = queue.popleft()
        current_state = current_path[-1]

        # Check if the agent reached its goal
        if current_state == goal_state:
            return current_path

        # Explore next possible actions if not already visited
        if current_state not in visited:
            visited.add(current_state)
            for next_action in agent_workflow.get(current_state, []):
                new_path = list(current_path)
                new_path.append(next_action)
                queue.append(new_path)

    return None

# 3. RUN THE AGENT
if __name__ == "__main__":
    start = "New Lead Received"
    goal = "GOAL: Meeting Confirmed"

    print("🤖 Starting Day 1 AI Agent Simulation...\n")
    best_plan = find_fastest_action_plan(start, goal)

    if best_plan:
        print("✅ Fastest Action Plan Found:")
        for step_number, action in enumerate(best_plan, start=1):
            print(f"   Step {step_number}: {action}")
    else:
        print("❌ No valid path to goal found.")
