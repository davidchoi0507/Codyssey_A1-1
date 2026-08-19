# main.py - 나만의 프롬프트 관리 프로그램 (디자인 / 음악 / 영상)

# 초기 프롬프트 데이터 (3개 이상 등록)
prompts = [
    {
        "id": 1,
        "title": "미니멀 로고 디자인 생성",
        "category": "디자인",
        "content": "모던하고 미니멀한 느낌의 IT 스타트업 로고를 벡터 스타일로 생성해줘.",
        "favorite": True
    },
    {
        "id": 2,
        "title": "시네마틱 배경음악 프롬프트",
        "category": "음악",
        "content": "웅장한 오케스트라와 전자음악이 융합된 90BPM 웅장한 묵시록풍 BGM 생성.",
        "favorite": False
    },
    {
        "id": 3,
        "title": "유튜브 숏폼 영상 콘티 구성",
        "category": "영상",
        "content": "15초 분량의 몰입감 넘치는 꿀팁 소개 영상 숏폼 스토리보드 작성해줘.",
        "favorite": True
    }
]

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
        "favorite": False
    })
    print(f"✅ ID {new_id}번 프롬프트가 성공적으로 추가되었습니다!")

def show_list():
    """2. 전체 목록 보기 함수"""
    print("\n[📋 전체 프롬프트 목록]")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for p in prompts:
        fav_mark = "⭐" if p["favorite"] else "☆"
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
        fav_mark = "⭐" if p["favorite"] else "☆"
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

    fav_str = "등록됨 ⭐" if p["favorite"] else "미등록 ☆"
    print("\n" + "-"*40)
    print(f"ID: {p['id']}")
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {fav_str}")
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

    p["favorite"] = not p["favorite"]
    state = "등록" if p["favorite"] else "해제"
    print(f"✅ ID {p_id}번 프롬프트가 즐겨찾기에 {state} 되었습니다.")

def show_favorites():
    """7. 즐겨찾기 목록 보기 함수"""
    print("\n[⭐ 즐겨찾기 프롬프트 목록]")
    favs = [p for p in prompts if p["favorite"]]

    if not favs:
        print("즐겨찾기로 등록된 프롬프트가 없습니다.")
        return

    for p in favs:
        print(f"[{p['id']}] [{p['category']}] {p['title']}")

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
        elif choice == "0":
            print("\n👋 프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
            break
        else:
            print("\n⚠️ 올바른 번호를 입력해 주세요 (0~7).")

if __name__ == "__main__":
    main()
