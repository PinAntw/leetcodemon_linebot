import requests

def get_recent_questions(username):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json"
    }

    query = """
    query recentAcSubmissions($username: String!) {
      recentAcSubmissionList(username: $username, limit: 20) {
        title
        titleSlug
        timestamp
      }
      matchedUser(username: $username) {   
        languageProblemCount {      
        languageName     
        problemsSolved
        }
    }
    }
    """
    # query = """
    # query recentAcSubmissions($username: String!) {
    #   recentAcSubmissionList(username: $username, limit: 20) {
    #     title
    #     titleSlug
    #     timestamp
    #   }
    # }
    # """

    variables = {"username": username}
    payload = {
        "query": query,
        "variables": variables
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        submissions = response.json()["data"]["recentAcSubmissionList"]
        print(f"\n最近做過的題目（共 {len(submissions)} 題）")
        for item in submissions:
            link = f"https://leetcode.com/problems/{item['titleSlug']}/"
            print(f"{item['title']} → {link}")
        print("user資訊啦")
        submissions_user = response.json()["data"]["matchedUser"]["languageProblemCount"]
        for item in submissions_user:
            print(f"{item['languageName']} → {item['problemsSolved']}")
    else:
        print("查詢失敗，請確認帳號是否正確。")

# === 請在這裡填入 LeetCode 使用者名稱 ===
get_recent_questions("PinAn_Lee")