from sqlalchemy.orm import Mapped, mapped_column
from database.core import Base
import datetime

class ConfigBackup(Base):
    __tablename__ = "configs"

    id: Mapped[int] = mapped_column(primary_key=True)
    app_name: Mapped[str]
    content: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow)
    version: Mapped[int] = mapped_column(default=1)