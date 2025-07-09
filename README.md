# 贪吃蛇（Python pygame 版）

这是一个用 Python 和 pygame 实现的经典贪吃蛇游戏，支持中文界面和像素风格蛇身。

## 运行方法

1. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```
2. 运行游戏
   ```bash
   python snake.py
   ```

## 依赖说明
- Python 3.x
- pygame
- 字体文件：`static/NotoSansSC-Regular.ttf`（用于中文显示）

## 特色功能
- 经典像素风格蛇身，每节均等大小
- 支持中文分数和提示，界面美观
- 字体文件放在 static 目录下，跨平台兼容
- 代码简洁，易于二次开发
- **修复：最终得分统计不准确的问题，优化了主循环顺序，确保每次吃到食物都能正确计分**

## 资源说明
- 字体文件请自行下载并放入 static 目录
- 可自定义蛇头、蛇身贴图（如有需求）

---

如有问题或建议，欢迎在 Issues 区留言！