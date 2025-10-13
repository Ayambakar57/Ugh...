from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.branch import crud_branch
from app.schemas.branch import BranchCreate, BranchUpdate, BranchResponse

router = APIRouter()


@router.get("/", response_model=List[BranchResponse])
def read_branches(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    branches = crud_branch.get_multi(db, skip=skip, limit=limit)
    return branches


@router.get("/{branch_id}", response_model=BranchResponse)
def read_branch(
    branch_id: UUID,
    db: Session = Depends(get_db)
):
    branch = crud_branch.get(db, id=branch_id)
    if branch is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch


@router.post("/", response_model=BranchResponse, status_code=201)
def create_branch(
    branch: BranchCreate,
    db: Session = Depends(get_db)
):
    return crud_branch.create(db, obj_in=branch)


@router.put("/{branch_id}", response_model=BranchResponse)
def update_branch(
    branch_id: UUID,
    branch: BranchUpdate,
    db: Session = Depends(get_db)
):
    db_branch = crud_branch.get(db, id=branch_id)
    if db_branch is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return crud_branch.update(db, db_obj=db_branch, obj_in=branch)


@router.delete("/{branch_id}", response_model=BranchResponse)
def delete_branch(
    branch_id: UUID,
    db: Session = Depends(get_db)
):
    branch = crud_branch.get(db, id=branch_id)
    if branch is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return crud_branch.delete(db, id=branch_id)
