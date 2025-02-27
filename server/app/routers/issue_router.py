from fastapi import APIRouter
from controllers.issue.issue_controller import (get_all_issues, get_issue_by_id, create_issue, update_issue,)
from schemas.issue.issue_schema import IssueCreate, IssueUpdate, ResponseIssue


issueRouter = APIRouter()

@issueRouter.get("/issue")
def fetch_issues():
    return get_all_issues()

@issueRouter.get("/issue/{issue_id}")
def fetch_issue(issue_id:int):
    return get_issue_by_id(issue_id)

@issueRouter.post("/issue", response_model=ResponseIssue)
def add_issue(volume: IssueCreate):
    return create_issue(volume)

@issueRouter.put("/issue/{issue_id}")
def modify_issue(issue_id:int, volume:IssueUpdate):
    return update_issue(issue_id, volume)


    
    