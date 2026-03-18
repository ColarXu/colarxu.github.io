import os
import frontmatter

CONTENT_DIR = './content'

def remove_seo_descriptions():
    count = 0
    for root, dirs, files in os.walk(CONTENT_DIR):
        for name in files:
            if name.endswith(".md"):
                path = os.path.join(root, name)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        post = frontmatter.load(f)
                    
                    # 如果发现有 description 字段，直接删除
                    if 'description' in post.metadata:
                        del post.metadata['description']
                        with open(path, 'wb') as f:
                            frontmatter.dump(post, f)
                        print(f"🗑️ 已清除: {name}")
                        count += 1
                except Exception as e:
                    print(f"❌ 处理 {name} 出错: {e}")
    print(f"\n清理完成！共还原了 {count} 篇文章。")

if __name__ == "__main__":
    remove_seo_descriptions()
