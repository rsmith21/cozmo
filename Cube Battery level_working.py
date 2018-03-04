
# this script will print on the terminal screen the Robot internal battery voltage
# and Cozmo will speak alout  the cube's battery percentage capacity remaining.
# I have still to find out at what point the cube batteries fail
# Bob 25th Feb 2018



import asyncio
import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

async def log_cube_info(robot: cozmo.robot.Robot, cube_id):
    cube = robot.world.get_light_cube(cube_id)
    if cube is not None:
        # Wait for up to few seconds for the cube to have received battery level info
        for i in range(30):
            if cube.battery_voltage is None:
                if i == 0:
                    cozmo.logger.info("Cube %s waiting for battery info...", cube_id)
                await asyncio.sleep(0.5)
            else:
                break
        cozmo.logger.info("Cube %s battery = %s", cube_id, cube.battery_str)
        #await robot.say_text ("My internal Battery Voltage Currently is: %s" % robot.battery_voltage,).wait_for_completed()
        await robot.say_text ("cube %s battery = %s " %(cube_id, cube.battery_str)).wait_for_completed()
        print("cube %s battery = %s " %(cube_id, cube.battery_str))
        
    else:
        
        cozmo.logger.warning("Cube %s is not connected - check the battery.", cube_id)
        

async def cozmo_program(robot: cozmo.robot.Robot):
    
    print("My internal Battery Voltage Currently is: %.3f" % robot.battery_voltage)
    
    
    
    await log_cube_info(robot, LightCube1Id)  # looks like a paperclip
    await log_cube_info(robot, LightCube2Id)  # looks like a lamp / heart
    await log_cube_info(robot, LightCube3Id)  # looks like the letters 'ab' over 'T'
    await robot.say_text ("My internal Battery Voltage Currently is: %.3f Volts" % robot.battery_voltage,).wait_for_completed()

cozmo.robot.Robot.drive_off_charger_on_connect = False

cozmo.run_program(cozmo_program)
