# mul_agent
基于 FastAPI 构建高性能任务调度系统，设计多 Agent 架构，实现任务解耦与动态分发，集成 LLM（GPT）实现 AI Agent 自动决策能力，实现前后端分离架构，支持实时任务执行与结果展示，支持任务类型扩展（插件化 Agent）

怎么跑（很关键）
① 启动后端cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
② 配置 AI Keyexport OPENAI_API_KEY=你的key
③ 打开前端直接打开：frontend/index.html
