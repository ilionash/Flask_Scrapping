import csv

def save_to_file(jobs, word):
  f = open(f"{word}.csv", "w")
  w = csv.writer(f)
  w.writerow(["title", "company", "location", "link"])
  for job in jobs:
    w.writerow(list(job.values()))
  
  return