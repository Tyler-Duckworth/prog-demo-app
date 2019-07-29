import wpilib
from wpilib.command.subsystem import Subsystem
from rev import CANSparkMax, MotorType

from commands.followjoystick import FollowJoystick
import pytest


class Drivetrain(Subsystem):
    """
    This example subsystem controls a single Talon in PercentVBus mode.
    """

    def __init__(self):
        """Instantiates the motor object."""

        super().__init__("SingleMotor")

        self.m_lfront = CANSparkMax(4, MotorType.kBrushless)
        self.m_lrear = CANSparkMax(1, MotorType.kBrushless)
        self.m_rfront = CANSparkMax(2, MotorType.kBrushless)
        self.m_rrear = CANSparkMax(3, MotorType.kBrushless)
        
        # self.m_lrear.follow(self.m_lfront, invert=True)
        # self.m_rrear.follow(self.m_rfront, invert=True)

        self.l_pid = self.m_lfront.getPIDController()
        self.r_pid = self.m_rfront.getPIDController()
        self.l_enc = self.m_lfront.getEncoder()
        self.r_enc = self.m_rfront.getEncoder()

        self.kP = 0.1
        self.kI = 1e-4
        self.kD = 0
        self.kIz = 0
        self.kFF = 0
        self.kMinOutput = -1
        self.kMaxOutput = 1

        self.l_pid.setP(self.kP)
        self.l_pid.setI(self.kI)
        self.l_pid.setD(self.kD)
        self.l_pid.setIZone(self.kIz)
        self.l_pid.setFF(self.kFF)
        self.l_pid.setOutputRange(self.kMinOutput, self.kMaxOutput)

        # self.r_pid.setP(self.kP)
        # self.r_pid.setI(self.kI)
        # self.r_pid.setD(self.kD)
        # self.r_pid.setIZone(self.kIz)
        # self.r_pid.setFF(self.kFF)
        # self.r_pid.setOutputRange(self.kMinOutput, self.kMaxOutput)

        # Push PID Coefficients to SmartDashboard
        wpilib.SmartDashboard.putNumber("P Gain", self.kP)
        wpilib.SmartDashboard.putNumber("I Gain", self.kI)
        wpilib.SmartDashboard.putNumber("D Gain", self.kD)
        wpilib.SmartDashboard.putNumber("I Zone", self.kIz)
        wpilib.SmartDashboard.putNumber("Feed Forward", self.kFF)
        wpilib.SmartDashboard.putNumber("Min Output", self.kMinOutput)
        wpilib.SmartDashboard.putNumber("Max Output", self.kMaxOutput)
        wpilib.SmartDashboard.putNumber("Set Rotations", 0)

    def setSpeed(self, l_speed, r_speed):
        self.m_lfront.set(l_speed)
        self.m_rfront.set(r_speed)

    def setPID(self, setpoint):
        self.pidController.setReference(setpoint, rev.ControlType.kPosition)

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())
