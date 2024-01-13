from magicbot import feedback, tunable


class Shooter:
    shoot_speed = tunable(1.0)  # speed is tunable via NetworkTables

    def __init__(self) -> None:
        self.deploying = False

    def deploy(self) -> None:
        # Start spinning up the motors to get ready to shoot
        self.deploying = True

    def shoot(self) -> None:
        # Shoot the game piece
        pass

    @feedback
    def is_ready(self) -> bool:
        # Check if the shooter is the correct speed to shoot
        return True

    def execute(self) -> None:
        if self.deploying:
            if self.is_ready():
                self.shoot()
                self.deploying = False
        else:
            # set the shooter speed to 0
            pass
