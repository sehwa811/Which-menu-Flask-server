from flask import Flask, request, jsonify
import random

menus = {
  "한식": {
    "면": {
      "좋아요": ["비빔냉면", "열무비빔국수", "쫄면"],
      "싫어요": ["잔치국수", "바지락칼국수", "냉면"]
    },
    "밥": {
      "좋아요": ["김치볶음밥", "비빔밥", "제육볶음", "김치찌개", "부대찌개"],
      "싫어요": ["불고기덮밥", "백반", "돈까스"]
    }
  },
  "아시안": {
    "면": {
        "좋아요": ["짬뽕", "탄탄면", "똠양꿍", "마라탕"],
        "싫어요": ["우동", "차슈라멘", "짜장면", "소고기 쌀국수", "팟타이", "미고랭", "야키소바"]
      },
      "밥": {
        "좋아요": ["나시고랭"],
        "싫어요": ["규동", "부타동", "중국식 볶음밥", "초밥", "커리"]
      }
  }, 
  "양식": {
    "면": {
        "좋아요": ["아라비아따 파스타"],
        "싫어요": ["크림파스타", "봉골레 파스타", "토마토 파스타"]
      },
      "밥": {
        "좋아요": ["빠에야"],
        "싫어요": ["리조또", "빠에야", "필라프"]
      }
  },
  "그 외": [
      "샌드위치", "타코", "케밥", "피자", "포케", "샐러드볼"
  ]
}

app = Flask(__name__)

@app.route("/pt", methods = ['POST'])
def menu():
    ctr = request.form.get('ctr')
    ndl = request.form.get('ndl')
    spc = request.form.get('spc')
    which_con = menus[ctr]
    if len(which_con) == 6:
        return jsonify(random.choice(which_con))
    else:
      type_food = which_con[ndl]
      spc_ok = type_food[spc]
      return jsonify(random.choice(spc_ok))

if __name__ == '__main__':
    app.run(debug=True)