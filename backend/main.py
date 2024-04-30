import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# SQLAlchemy configurations
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy models
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI app instance
app = FastAPI()

# Pydantic models
class PostCreate(BaseModel):
    title: str
    content: str

class PostUpdate(BaseModel):
    title: str
    content: str

# CRUD operations
# Create (Create post)
@app.post('/posts/', response_model=Post)
async def create_post(post_data: PostCreate):
    db = SessionLocal()
    db_post = Post(**post_data.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Read (Get all posts)
@app.get('/posts/', response_model=list[Post])
async def get_posts():
    db = SessionLocal()
    return db.query(Post).all()

# Read (Get a post by id)
@app.get('/posts/{post_id}', response_model=Post)
async def get_post(post_id: int):
    db = SessionLocal()
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

# Update (Edit a post)
@app.put('/posts/{post_id}', response_model=Post)
async def update_post(post_id: int, post_data: PostUpdate):
    db = SessionLocal()
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db_post.title = post_data.title
    db_post.content = post_data.content
    db.commit()
    return db_post

# Delete (Delete a post)
@app.delete('/posts/{post_id}')
async def delete_post(post_id: int):
    db = SessionLocal()
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app)
