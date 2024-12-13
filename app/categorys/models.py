from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, str_uniq, int_pk


class Category(Base):
    id: Mapped[int_pk]
    name: Mapped[str]

    films: Mapped[list['Film']] = relationship(
        back_populates="categorys",
        secondary="filmcategorys"
    )

    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"category_name={self.name!r}")

    def __repr__(self):
        return str(self)