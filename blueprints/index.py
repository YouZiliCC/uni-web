from flask import Blueprint, render_template, current_app
from database.actions import list_all_projects

index_bp = Blueprint("index", __name__)


@index_bp.route("/", methods=["GET"])
def index():
    """主页 - 展示精选项目"""
    projects = list_all_projects()
    # 按点赞数排序，取前6个作为精选
    featured_projects = sorted(
        projects, 
        key=lambda p: len(p.stars) if p.stars else 0, 
        reverse=True
    )[:6]
    
    external_url = (
        current_app.config.get("SERVER_PROTOCOL", "http")
        + "://"
        + current_app.config.get("SERVER_DOMAIN", "localhost")
    )
    
    return render_template(
        "index.html", 
        featured_projects=featured_projects,
        total_projects=len(projects),
        external_url=external_url
    )


@index_bp.route("/docs", methods=["GET"])
def docs():
    """使用帮助页面"""
    return render_template("docs.html")
