from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import DateTime, func, String, Float


# 1. 创建异步引擎
DATABASE_URL = "mysql+aiomysql://root:123%40Wangguochen@localhost:3306/FastAPI_demo"
engine = create_async_engine(
    DATABASE_URL,
    echo=True, # 可选, 输出日志
    pool_size=5,
    max_overflow=20
)


# 2. 基类 + 模型类
class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), default=func.now, comment="创建时间")
    update_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), default=func.now, onupdate=func.now(), comment="更新时间")


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, comment="书籍ID")
    title: Mapped[str] = mapped_column(String(100), comment="书籍标题")
    author: Mapped[str] = mapped_column(String(100), comment="书籍作者")
    price: Mapped[float] = mapped_column(Float, comment="书籍价格")
    publisher: Mapped[str] = mapped_column(String(100), comment="书籍出版社")


# 3. 建表
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 应用启动时执行
    await create_tables()
    yield
    # 应用关闭时执行
    await engine.dispose()


app = FastAPI(lifespan=lifespan)