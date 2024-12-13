from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, str_uniq, int_pk


class Film(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    film_link: Mapped[str]

    categorys: Mapped[list['Category']] = relationship(
        back_populates="films",
        secondary="filmcategorys"
    )

    directors: Mapped[list['Director']] = relationship(
        back_populates="films",
        secondary="filmdirectors"
    )

    actors: Mapped[list['Actor']] = relationship(
        back_populates="films",
        secondary="filmactors"
    )

    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"film_name={self.name!r}, "
                f"link={self.film_link!r})")

    def __repr__(self):
        return str(self)