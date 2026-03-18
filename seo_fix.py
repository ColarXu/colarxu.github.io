import os
import frontmatter
import re

# 1. 设置你的文章存放路径
CONTENT_DIR = './content'

def clean_text(text):
    """清理 Markdown 杂质，只保留纯文本用于 SEO"""
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)  # 删图片
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)   # 删链接
    text = re.sub(r'<.*?>', '', text)            # 删 HTML 标签
    text = re.sub(r'#+\s+', '', text)            # 删标题符
    text = re.sub(r'[\-\*\+]\s+', '', text)      # 删列表符
    text = text.replace('`', '').replace('\n', ' ').strip()
    return text

def run_seo_injection():
    processed_count = 0
    skipped_count = 0

    for root, dirs, files in os.walk(CONTENT_DIR):
        for name in files:
            if name.endswith(".md"):
                path = os.path.join(root, name)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        post = frontmatter.load(f)
                    
                    # 只有在 description 为空或不存在时才操作
                    if not post.get('description'):
                        raw_content = post.content
                        pure_text = clean_text(raw_content)
                        
                        # 截取前 120 字，末尾加省略号
                        summary = pure_text[:120].strip() + "..."
                        post['description'] = summary
                        
                        # 写回文件
                        with open(path, 'wb') as f:
                            frontmatter.dump(post, f)
                        print(f"✅ 已注入描述: {name}")
                        processed_count += 1
                    else:
                        skipped_count += 1
                except Exception as e:
                    print(f"❌ 出错 {name}: {e}")

    print(f"\n任务完成！")
    print(f"新处理: {processed_count} 篇")
    print(f"已跳过: {skipped_count} 篇（已有描述）")

if __name__ == "__main__":
    run_seo_injection()
