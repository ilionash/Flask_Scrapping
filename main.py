from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from expoter import save_to_file as save

app = Flask("Flask")

db = {}

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    word = request.args.get("word")

    if word:
      word = word.lower()
      
      if word in db:
        print("It is in DB")
        jobs = db.get(word)
      else:
        print("It isn't in DB")
        jobs = get_jobs(word)
        db[word] = jobs

    else:
      return redirect("/")

    return render_template(
      "report.html",
      searchingBy = word,
      jobs = jobs,
      resultsNumber = len(jobs)
    )


@app.route("/export")
def export():
  try:
    word = request.args.get("word")
    
    if not word:
      print("Not Word!!!")
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    
    save(jobs, word)

    return send_file(
      f"{word}.csv",
      mimetype='text/csv',
      as_attachment=True,
      attachment_filename=f"{word}.csv"
    )

  except:
    return redirect("/")

  return

app.run(host="0.0.0.0")
