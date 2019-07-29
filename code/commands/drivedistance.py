from wpilib.command import Command
import subsystems


class DriveDistance(Command):
    """
    This command will read the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.
    """

    def __init__(self, distance):
        super().__init__("DriveDistance")

        self.requires(subsystems.drivetrain)
        self.distance = distance

    def execute(self):
        subsystems.drivetrain.setPID(self.distance)

    def end(self):
        subsystems.drivetrain.setSpeed(0, 0)

    def interrupted(self):
        self.end()
