from wpilib.command import Command
import subsystems
import oi


class FollowJoystick(Command):
    """
    This command will read the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.
    """

    def __init__(self):
        super().__init__("Follow Joystick")

        self.requires(subsystems.drivetrain)

    def execute(self):
        subsystems.drivetrain.setSpeed(oi.joystick.getX(),
                                       oi.joystick.getY())
