"""Main file
This file is used to evaluate a model for jaco's non-vision servo
grasp task. If there is no model, this file will train one

"""

########################################################################
# Get the package path
########################################################################
import sys
import os

package_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(package_path)
os.chdir(package_path)
########################################################################
# Train a model
########################################################################
from envs import KukaVisionServoGraspEnv
from core.model import GPModel
import traceback
import os


if __name__ == "__main__":
    env = KukaVisionServoGraspEnv(
        render=True,
        width=128,
        height=128,
        show_image=False,
    )
    obs = env.reset()
    model = GPModel(env=env, total_time_steps=5000000)
    try:
        model.evaluate(record=False)
    except BaseException as e:
        traceback.print_exc()
