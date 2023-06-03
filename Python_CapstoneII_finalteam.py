# WELCOME SCREEN
print("--------------------------------------------------")
print("\n           Capstone Project II")
print("\n--------------------------------------------------")
print("\n**************************************************")
print("    Tetravaal Industries - SCOUT patrol robot     ")
print("**************************************************")
print("\nStarting up....")
print("FIRMWARE LOADED [OK]")
print("SOFTWARE LOADED [OK]")
print("\nBEGIN BOOT SEQUENCE CHECKS")
print("----------------------------")

#import random module
import random

#--------------- OOP - Inheritence ------------------------#

# ------- Parent Class - Robot ---------------------# 
class Robot:
    def _init_(self, status):        
      self.status = status

   
# ------- Child Class - Antennas ---------------------# 
class Antennas(Robot):
    def check_antennas(self, status):
        if status == 0:
          return "[FAIL] SCOUT cannot operate."
        elif status == 1:
          return "[OK]"
        elif status == 2:
          return "[WARN] SCOUT service degraded. Repair or replace soon."

# ------- Child Class - Camera Apparatus---------------------# 
class Camera_Apparatus(Robot):
    def check_camera_apparatus(self, status):
        if status == 0:
          return "[FAIL] SCOUT cannot operate."
        elif status == 1:
          return "[OK]"
        elif status == 2:
          return "[WARN] SCOUT service degraded. Repair or replace soon."

# ------- Child Class - Arms---------------------# 
class Arms(Robot):
    def check_arms(self, status):
        if status == 0:
          return "[FAIL] SCOUT cannot operate."
        elif status == 1:
          return "[OK]"
        elif status == 2:
          return "[WARN] SCOUT service degraded. Repair or replace soon."

# ------- Child Class - Torso---------------------# 
class Torso(Robot):
    def check_torso(self, status):
        if status == 0:
          return "[FAIL] SCOUT cannot operate."
        elif status == 1:
          return "[OK]"
        elif status == 2:
          return "[WARN] SCOUT service degraded. Repair or replace soon."
# ------- Child Class - Legs---------------------# 
class Legs(Robot):
    def check_legs(self, status):
        if status == 0:
          return "[FAIL] SCOUT cannot operate."
        elif status == 1:
          return "[OK]"
        elif status == 2:
          return "[WARN] SCOUT service degraded. Repair or replace soon."

# ------- Child Class -AINetworkLink ---------------------# 
class AINetworkLink(Robot):
    def check_network(self, status):
        if status == 0:
          return "[FAIL] SCOUT cannot operate."
        elif status == 1:
          return "[OK]"
        elif status == 2:
          return "[WARN] SCOUT service degraded. Repair or replace soon."


# Create robot instances
robotAntennas = Antennas()
robotCameraApparutus =  Camera_Apparatus()
robotArms = Arms()
robotTorso = Torso()
robotLegs = Legs()
robotConnection = AINetworkLink()

# Store different component statuses
antenna_status = robotAntennas.check_antennas(random.randint(0, 2))
camera_status = robotCameraApparutus.check_camera_apparatus(random.randint(0, 2))
arm_status = robotArms.check_arms(random.randint(0, 2))
torso_status = robotTorso.check_torso(random.randint(0, 2))
leg_status = robotLegs.check_legs(random.randint(0, 2))
connection_status = robotConnection.check_network(random.randint(0, 2))

# Print the result
print("Checking Antennas (L/R):        ", antenna_status)
print("Checking Camera apparatus:      ", camera_status)
print("Checking Arms (L/R):            ", arm_status)
print("Checking Torso:                 ", torso_status)
print("Checking legs:                  ", leg_status)
print("Checking Connection:            ", connection_status)

# Count the Success/Fail/Warn
success_cnt = 0
warn_cnt = 0
fail_cnt = 0

if antenna_status == '[OK]':
  success_cnt += 1
elif antenna_status == '[WARN] SCOUT service degraded. Repair or replace soon.':
  warn_cnt += 1
elif antenna_status == '[FAIL] SCOUT cannot operate.':
  fail_cnt += 1

if camera_status == '[OK]':
  success_cnt += 1
elif camera_status == '[WARN] SCOUT service degraded. Repair or replace soon.':
  warn_cnt += 1
elif camera_status == '[FAIL] SCOUT cannot operate.':
  fail_cnt += 1

if arm_status == '[OK]':
  success_cnt += 1
elif arm_status == '[WARN] SCOUT service degraded. Repair or replace soon.':
  warn_cnt += 1
elif arm_status == '[FAIL] SCOUT cannot operate.':
  fail_cnt += 1

if torso_status == '[OK]':
  success_cnt += 1
elif torso_status == '[WARN] SCOUT service degraded. Repair or replace soon.':
  warn_cnt += 1
elif torso_status == '[FAIL] SCOUT cannot operate.':
  fail_cnt += 1

if leg_status == '[OK]':
  success_cnt += 1
elif leg_status == '[WARN] SCOUT service degraded. Repair or replace soon.':
  warn_cnt += 1
elif leg_status == '[FAIL] SCOUT cannot operate.':
  fail_cnt += 1

if connection_status == '[OK]':
  success_cnt += 1
elif connection_status == '[WARN] SCOUT service degraded. Repair or replace soon.':
  warn_cnt += 1
elif connection_status == '[FAIL] SCOUT cannot operate.':
  fail_cnt += 1

# Print the Total Success/Fail/Warn counts based on sum of different component counts
print("\nChecks completed with: ",success_cnt, "[OK]", warn_cnt, "[WARN]", fail_cnt, "[FAIL]")

# Shut down SCOUT if there are any failure statuses or connection status is either warn or fail
if fail_cnt > 0 or connection_status != '[OK]':
  print("\nSCOUT CANNOT OPERATE DUE TO ONE OR MORE FAILURES. SHUTTING DOWN")
else:
  print("\nSCOUT IS OPERATIONAL.")
