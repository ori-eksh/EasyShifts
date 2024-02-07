from __future__ import annotations
from sqlalchemy.orm import Session
from Backend.db.controllers.base_controller import BaseController
from Backend.db.repositories.shifts_repository import ShiftsRepository
from Backend.db.services.shifts_service import ShiftsService


class ShiftsController(BaseController):
    """
    ShiftsController Class

    Controller class for managing shift entities.
    """

    def __init__(self, db: Session):
        """
        Initializes the ShiftsController with a database session.

        Parameters:
            db (Session): SQLAlchemy Session for database interactions.
        """
        self.repository = ShiftsRepository(db)
        self.service = ShiftsService(self.repository)
        super().__init__(self.repository, self.service)
