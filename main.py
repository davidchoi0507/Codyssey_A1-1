import json
import os

# main.py - 나만의 프롬프트 관리 프로그램 (디자인 / 음악 / 영상)

# 초기 프롬프트 데이터 (3개 이상 등록)
DATA_FILE = "prompts.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ 데이터 파일 형식이 잘못되어 초기화합니다.")
            return []
    # 파일이 없으면 기본 데이터 3개 반환
    return [
        {"id": 1, "title": "미니멀 로고 디자인 생성", "content": "모던하고 미니멀한 느낌의 IT 스타트업 로고를 벡터 스타일로 생성해줘.", "category": "디자인", "favorite": True, "views": 0},
        {"id": 2, "title": "시네마틱 배경음악 프롬프트", "content": "웅장한 오케스트라와 전자음악이 융합된 90BPM 웅장한 묵시록풍 BGM 생성.", "category": "음악", "favorite": False, "views": 0},
        {"id": 3, "title": "유튜브 숏폼 영상 콘티 구성", "content": "15초 분량의 몰입감 넘치는 꿀팁 소개 영상 숏폼 스토리보드 작성해줘.", "category": "영상", "favorite": True, "views": 0}
    ]

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=4)

prompts = load_data()

def show_menu():
    """메뉴 출력 함수"""
    print("\n" + "="*45)
    print("🎨 [David's 프롬프트 관리 프로그램] 🎬")
    print("="*45)
    print("1. 프롬프트 추가")
    print("2. 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 토글 (등록/해제)")
    print("7. 즐겨찾기 목록")
    print("8. 마크다운으로 내보내기")
    print("9. 프롬프트 삭제")
    print("10. 조회수 TOP 목록")
    print("0. 종료")
    print("="*45)

def add_prompt():
    """1. 프롬프트 추가 함수"""
    print("\n[➕ 새 프롬프트 추가]")
    title = input("제목을 입력하세요: ").strip()
    category = input("카테고리를 입력하세요 (디자인/음악/영상 등): ").strip()
    content = input("프롬프트 내용을 입력하세요: ").strip()

    if not title or not content:
        print("⚠️ 제목과 내용은 필수 입력 항목입니다.")
        return

    new_id = len(prompts) + 1 if prompts else 1
    prompts.append({
        "id": new_id,
        "title": title,
        "category": category if category else "기타",
        "content": content,
        "favorite": False,
        "views": 0
    })
    
    save_data()
    print(f"✅ ID {new_id}번 프롬프트가 성공적으로 추가되었습니다!")

def show_list():
    """2. 전체 목록 보기 함수"""
    print("\n[📋 전체 프롬프트 목록]")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for p in prompts:
        fav_mark = "⭐" if p.get("favorite", False) else "☆"
        print(f"[{p['id']}] {fav_mark} [{p['category']}] {p['title']}")

def show_by_category():
    """3. 카테고리별 조회 함수"""
    print("\n[📂 카테고리별 조회]")
    cat = input("조회할 카테고리를 입력하세요 (예: 디자인): ").strip()
    filtered = [p for p in prompts if p["category"].lower() == cat.lower()]

    if not filtered:
        print(f"'{cat}' 카테고리에 해당하는 프롬프트가 없습니다.")
        return

    for p in filtered:
        fav_mark = "⭐" if p.get("favorite", False) else "☆"
        print(f"[{p['id']}] {fav_mark} {p['title']} - {p['content'][:30]}...")

def search_prompt():
    """4. 검색 함수"""
    print("\n[🔍 프롬프트 검색]")
    keyword = input("검색어를 입력하세요 (제목/내용): ").strip().lower()
    results = [p for p in prompts if keyword in p["title"].lower() or keyword in p["content"].lower()]

    if not results:
        print(f"'{keyword}' 검색 결과를 찾을 수 없습니다.")
        return

    print(f"총 {len(results)}건의 검색 결과:")
    for p in results:
        print(f"[{p['id']}] [{p['category']}] {p['title']}")

def view_detail():
    """5. 상세 보기 함수"""
    print("\n[🔎 프롬프트 상세 보기]")
    try:
        p_id = int(input("조회할 프롬프트 ID를 입력하세요: "))
    except ValueError:
        print("⚠️ 숫자로 입력해주세요.")
        return

    p = next((item for item in prompts if item["id"] == p_id), None)
    if not p:
        print("해당 ID의 프롬프트를 찾을 수 없습니다.")
        return

    # 조회수 증가 및 저장
    p["views"] = p.get("views", 0) + 1
    save_data()

    fav_str = "등록됨 ⭐" if p.get("favorite", False) else "미등록 ☆"
    print("\n" + "-"*40)
    print(f"ID: {p['id']}")
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {fav_str}")
    print(f"조회수: {p['views']}회") 
    print(f"내용:\n{p['content']}")
    print("-" * 40)

def toggle_favorite():
    """6. 즐겨찾기 토글 함수"""
    print("\n[⭐ 즐겨찾기 관리]")
    try:
        p_id = int(input("즐겨찾기를 변경할 프롬프트 ID를 입력하세요: "))
    except ValueError:
        print("⚠️ 숫자로 입력해주세요.")
        return

    p = next((item for item in prompts if item["id"] == p_id), None)
    if not p:
        print("해당 ID의 프롬프트를 찾을 수 없습니다.")
        return

    p["favorite"] = not p.get("favorite", False)
    save_data()
    
    state = "등록" if p["favorite"] else "해제"
    print(f"✅ ID {p_id}번 프롬프트가 즐겨찾기에 {state} 되었습니다.")

def show_favorites():
    """7. 즐겨찾기 목록 보기 함수"""
    print("\n[⭐ 즐겨찾기 프롬프트 목록]")
    favs = [p for p in prompts if p.get("favorite", False)]

    if not favs:
        print("즐겨찾기로 등록된 프롬프트가 없습니다.")
        return

    for p in favs:
        print(f"[{p['id']}] [{p['category']}] {p['title']}")

def export_by_category():
    print("\n--- [8. 카테고리별 Markdown 내보내기] ---")
    categories = list(set(p["category"] for p in prompts))
    
    if not categories:
        print("ℹ️ 내보낼 프롬프트가 없습니다.\n")
        return

    for category in categories:
        filename = f"{category.replace(' ', '_')}_prompts.md"
        category_prompts = [p for p in prompts if p["category"] == category]
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {category} 프롬프트 모음\n\n")
            for p in category_prompts:
                fav = "⭐" if p.get("favorite", False) else ""
                f.write(f"## [{p['id']}] {p['title']} {fav}\n")
                f.write(f"**조회수:** {p.get('views', 0)}\n\n")
                f.write(f"```text\n{p['content']}\n```\n\n---\n")
    print(f"✅ {len(categories)}개 카테고리의 Markdown 파일 생성이 완료되었습니다.\n")

def delete_prompt():
    print("\n--- [9. 프롬프트 삭제] ---")
    try:
        pid = int(input("삭제할 프롬프트 ID: ").strip())
    except ValueError:
        print("⚠️ 숫자로 입력해주세요.\n")
        return

    global prompts
    original_len = len(prompts)
    prompts = [p for p in prompts if p["id"] != pid]

    if len(prompts) < original_len:
        save_data()
        print(f"✅ 프롬프트 #{pid} 삭제가 완료되었습니다.\n")
    else:
        print(f"⚠️ ID {pid}번 프롬프트를 찾을 수 없습니다.\n")

def show_top_views():
    print("\n--- [10. 조회수 TOP 목록] ---")
    if not prompts:
        print("ℹ️ 등록된 프롬프트가 없습니다.\n")
        return
    
    # 조회수(views) 기준으로 내림차순 정렬
    sorted_prompts = sorted(prompts, key=lambda x: x.get("views", 0), reverse=True)
    
    for p in sorted_prompts:
        fav_icon = "⭐" if p.get("favorite", False) else "☆"
        print(f"[{p['id']}] 👁️ 조회 {p.get('views', 0)}회 | {fav_icon} [{p['category']}] {p['title']}")
    print()

def main():
    """메인 실행 루프"""
    while True:
        show_menu()
        choice = input("원하는 메뉴 번호를 선택하세요: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            view_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "8":
            export_by_category()
        elif choice == "9":
            delete_prompt()
        elif choice == "10":
            show_top_views()
        elif choice == "0":
            print("\n👋 프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
            break
        else:
            print("\n⚠️ 올바른 번호를 입력해 주세요 (0~10).")

if __name__ == "__main__":
    main()
