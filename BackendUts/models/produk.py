from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base


class Produk(Base):
    __tablename__ = "produk"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nama: Mapped[str] = mapped_column(String(255), nullable=False)
    harga: Mapped[int] = mapped_column(Integer, nullable=False)
    stok: Mapped[int] = mapped_column(Integer, nullable=False)
    gambar: Mapped[str] = mapped_column(String(255), nullable=True)