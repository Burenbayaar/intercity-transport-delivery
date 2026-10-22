# Лаб 6-г яг дарааллаар хийх заавар

Доорх командуудыг Windows-ийн PowerShell эсвэл VS Code-ийн PowerShell терминалд ажиллуулна. `python --version` ажиллахгүй бол Python 3-ыг суулгасны дараа үргэлжлүүлнэ. Эсвэл `py --version` ажиллаж байвал бүх `python` командыг `py` болгож солино.

## 0. Хосоо сонгож, өөр өөр бүртгэлээр ажиллах

Баг 3 хүнтэй боловч энэ дасгалд 2 хүн оролцоно. Жишээ хуваарилалт: A — Ж.Булган; B — Ж.Буянхишиг. Үүнийг бодит ажиллах хоёр хүнээр тохируулж болно. Гурав дахь гишүүн ажиглах эсвэл нэмэлт review хийж болно; шаардах хоёр хүний ажлыг орлохгүй.

- A, B тусдаа GitHub бүртгэлээрээ ажиллана. Нэг хүний хоёр branch нь хосын review хийсэн нотолгоо болохгүй.
- Хоёуланд нь repository дээр branch push хийх эрх хэрэгтэй. Эрхгүй гишүүнийг эзэмшигч `Settings → Collaborators` хэсгээс нэмж, тэр хүн урилгаа хүлээн авна. Дасгалын энэ заавар нэг repository доторх collaborator workflow ашиглана.
- `git config user.name`, `git config user.email` командаар тус тусын Git identity-г шалгана. Бусдын нэрийг өөрийн commit-д тавихгүй. Username/password/token-оо README, screenshot, commit-д оруулахгүй.
- Өөрчлөлттэй файл байвал устгахгүй; эхлээд өөрийн ажлаа тусдаа commit эсвэл stash-д хадгална.

A-ийн компьютер дээр өөрийн бодит замд орно. Өмнө ашиглаж байсан зам таарч байвал:

```powershell
cd "C:\Users\zolbi\Downloads\intercity-transport-delivery\intercity-transport-delivery"
git status
git remote -v
```

Зам өөр бол VS Code-оор зөв repository хавтсыг нээгээд терминал ашиглана. `origin` нь энэ төслийн repository мөн эсэхийг шалгана.

## 1. A: нийтлэг эхийг main дээр нэг удаа бэлдэх

```powershell
git switch main
git pull --ff-only origin main
```

Татсан багцын **lab6 хавтсыг** repository-ийн үндсэн хавтас руу хуулна. Өмнө нь lab6 байгаа бол шууд дарж хуулахгүй: эхлээд агуулгыг харьцуулж хадгална. Бусад lab, README-г солихгүй.

```powershell
python -m unittest discover -s lab6/tests -v
git diff --check
git add lab6
git diff --cached --stat
git commit -m "Add Lab 6 branching and review starter"
git push origin main
```

**Хүлээх үр дүн:** 5 тест OK; lab6 эх файлууд GitHub main дээр харагдана. Энэ эхийг push хийхэд хоёр feature бүрэн болоогүй байх нь зориудын сургалтын нөхцөл юм.

Main-д шууд push хийхийг repository хориглодог бол хамгаалалтыг унтраахгүй. Энэ нийтлэг эхийг тусдаа setup branch/PR-аар main-д оруулсны дараа 2-р алхмыг эхлүүлнэ.

README-ийн лабын хүснэгтэд хүсвэл `| 6 | [Git Branching, Merge Conflict, Code Review](lab6/README.md) |` гэсэн мөр нэмээд тусад нь commit хийнэ. Бусад README агуулгыг өөрчлөх шаардлагагүй.

## 2. A: эхний feature branch ба commit

```powershell
git switch main
git pull --ff-only origin main
git switch -c feature/seat-validation
Copy-Item lab6\variants\seat-validation.py lab6\booking.py
Copy-Item lab6\variants\test_seat_validation.py lab6\tests\test_seat_validation.py
python -m unittest discover -s lab6/tests -v
git diff --check
git diff -- lab6/booking.py
git add lab6/booking.py lab6/tests/test_seat_validation.py
git commit -m "Validate positive seat counts and available capacity"
git push -u origin feature/seat-validation
```

**Хүлээх үр дүн:** 10 тест OK. Энэ PR-ийг одоохондоо merge хийхгүй.

## 3. B: мөн адил эх main-аас хоёр дахь feature branch үүсгэх

B өөрийн компьютер дээр repository-г clone хийгээгүй бол зөвхөн нэг удаа:

```powershell
git clone https://github.com/Buyka1108/intercity-transport-delivery.git
cd intercity-transport-delivery
```

Өмнө clone хийсэн бол өөрийн repository хавтас руу орно. Дараа нь:

```powershell
git switch main
git pull --ff-only origin main
git switch -c feature/trip-status
Copy-Item lab6\variants\trip-status.py lab6\booking.py
Copy-Item lab6\variants\test_trip_status.py lab6\tests\test_trip_status.py
python -m unittest discover -s lab6/tests -v
git diff --check
git diff -- lab6/booking.py
git add lab6/booking.py lab6/tests/test_trip_status.py
git commit -m "Allow bookings only for OPEN trips"
git push -u origin feature/trip-status
```

**Хүлээх үр дүн:** 9 тест OK. Хоёр feature-ийн `booking.py` файлын сүүлийн `return` мөр өөр өөр болсон байна.

**Чухал:** B-ийн branch болон commit бэлэн болохоос өмнө A-ийн PR-ийг main руу merge хийж болохгүй. Хоёр branch ижил нийтлэг эхээс үүссэн үед зориудын conflict баталгаатай гарна. `pull --ff-only` алдаа өгвөл force/reset хийхгүй; гаралтыг шалгаж байж үргэлжлүүлнэ.

## 4. A, B: тус бүр нэг PR үүсгэх

Repository → **Pull requests → New pull request**.

| PR | base | compare | Гарчиг | Description |
|---|---|---|---|---|
| A | `main` | `feature/seat-validation` | `Validate positive seat counts and available capacity` | `lab6/review/pr-seat-validation.md` |
| B | `main` | `feature/trip-status` | `Allow bookings only for OPEN trips` | `lab6/review/pr-trip-status.md` |

`Create pull request` дарна. **Хоёр PR хоёулаа нээгдсэний дараа** 5-р алхам руу орно. Нэг feature-ийг нөгөө feature рүү PR болгож болохгүй.

## 5. B: A-ийн PR дээр review хийх

B өөрийн GitHub бүртгэлээр A-ийн PR → **Files changed** хэсгийг нээнэ. Өөрчлөгдсөн код, тестийг уншаад мөрийн хажуугийн `+` товчоор **дор хаяж хоёр утгатай comment** бичнэ. `lab6/review/review-guide.md`-д шалгах зүйл, асуултын жишээ бий; шалгаагүй зүйлээ шалгасан гэж бичихгүй.

Орон нутагтаа A-ийн branch-ийг шалгах бол B өөрийн ажлаа commit/push хийсний дараа:

```powershell
git fetch origin
git switch -c review/seat-validation --track origin/feature/seat-validation
python -m unittest discover -s lab6/tests -v
```

Хэрэв энэ review branch өмнө нь үүссэн бол дахин `-c` хийхгүй, тухайн branch руу `git switch` хийнэ.

GitHub дээр review эхлүүлсэн бол comment-уудаа бичээд **Review changes → Submit review** дарж нийтэлнэ. Зөв байвал `Approve`, асуудалтай бол `Request changes` сонгоно. A шаардлагатай засварыг өөрийн feature branch дээр commit/push хийж, B дахин шалгана. PR-ийн зохиогч өөрийн PR-д өгсөн comment нь нөгөө хүний review-г орлохгүй.

## 6. A: эхний PR-ийг main руу merge хийх

A-ийн PR дээр B-ийн хоёр comment нийтлэгдсэн, шаардлагатай засвар дууссан, тест амжилттай байгааг шалгана. **Merge pull request → Confirm merge** дарна. Merge төрлөөс сонгож болох бол **Create a merge commit** ашиглана. Branch-ийг нотолгоогоо автал устгахгүй.

**Хүлээх үр дүн:** A-ийн PR `Merged` болно. Main нь суудлын эерэг тооны дүрэмтэй боловч аяллын OPEN дүрэм хараахан ороогүй байна. B-ийн PR одоо conflict-тэй болно.

## 7. B: main-ийг өөрийн branch руу merge хийж conflict гаргах

B өөрийн компьютерт:

```powershell
git switch feature/trip-status
git status
git fetch origin
git merge origin/main
```

`git status` цэвэр байх үед merge хийнэ. **Хүлээх үр дүн:** `CONFLICT (content): Merge conflict in lab6/booking.py`. Энэ үед комманд алдааны кодтой дуусах нь даалгаврын зориудын үр дүн; дахин merge/pull дараалан хийхгүй.

```powershell
git status
Get-Content lab6/booking.py
```

Conflict marker-тай файл болон терминалын conflict мэдэгдлийн screenshot-оо `lab6/evidence/` дотор хадгалж болно. Marker-тай файлыг шийдээгүй чигээр commit/push хийхгүй.

B-ийн branch дээрх мөр нь `HEAD`, шинээр орж ирж буй суудлын дүрэм нь `origin/main` хэсэгт харагдана:

```text
  <<<<<<< HEAD
    return trip_status == "OPEN" and seat_count <= available_seats
  =======
    return 0 < seat_count <= available_seats
  >>>>>>> origin/main
```

Энэ блокийг дараах **хоёр дүрмийг хамтад нь хадгалсан** мөрөөр солино:

```python
    return trip_status == "OPEN" and 0 < seat_count <= available_seats
```

Зөвхөн `Accept Current` эсвэл `Accept Incoming` сонговол нэг дүрэм алга болно. `Accept Both` хийж хоёр `return` дараалуулах нь мөн буруу: хоёр дахь нь ажиллахгүй.

Дээрхийг гараар зассаны дараа бүрэн шийдлийн эхтэй харьцуулна. Сургалтын энэ файлын хувьд бэлдсэн шийдлийг бүхэлд нь авах хувилбар:

```powershell
Copy-Item lab6\variants\resolved.py lab6\booking.py
Copy-Item lab6\variants\test_combined_policy.py lab6\tests\test_combined_policy.py
python -m unittest discover -s lab6/tests -v
git diff --check
git diff -- lab6/booking.py
git add lab6/booking.py lab6/tests/test_combined_policy.py
git diff --cached --check
git commit -m "Resolve conflict and preserve seat and OPEN-trip rules"
git push origin feature/trip-status
```

**Хүлээх үр дүн:** 18 тест OK; merge commit үүснэ; B-ийн PR дээрх conflict арилна. Хэрэв review-ээр өөр нэмэлт засвар хийсэн бол `resolved.py`-г сохроор хуулж тэр засварыг дарж болохгүй — нэгтгэхдээ хадгална.

## 8. A: B-ийн шинэчлэгдсэн PR дээр review хийх

A өөрийн бүртгэлээр B-ийн PR → **Files changed** хэсгийг уншина. **Дор хаяж хоёр бодитой comment** бичиж нийтэлнэ. Ялангуяа хоёр дүрэм хамт үлдсэн эсэх, 18 тестийн нийлмэл хувилбаруудыг шалгана.

A орон нутагтаа шалгахдаа өөрийн өөрчлөлтүүдээ эхлээд commit хийгээд:

```powershell
git fetch origin
git switch -c review/trip-status --track origin/feature/trip-status
python -m unittest discover -s lab6/tests -v
git diff --check
```

Review зөв бол **Approve → Submit review** дарна. Асуудал байвал B өөрийн branch дээр засаж commit/push хийгээд A дахин шалгана.

## 9. B: хоёр дахь PR-ийг main руу merge хийх

Review дууссан, conflict байхгүй, тест OK болсон үед B-ийн PR дээр **Merge pull request → Confirm merge** дарна. Боломжтой бол **Create a merge commit** сонгоно.

A, B хоёул өөр өөрийн repository дээр:

```powershell
git switch main
git pull --ff-only origin main
python -m unittest discover -s lab6/tests -v
git log --graph --oneline --decorate --all -20
```

**Хүлээх үр дүн:** main дээр 18 тест OK, хоёр PR хоёулаа `Merged`, хоёр feature-ийн дүрэм хамт байна. Merge дууссан PR-д нэмэлт өөрчлөлт оруулахгүй.

## 10. A: нотолгоогоо бүрдүүлээд илгээх

`lab6/evidence/report.md` дахь бөглөөгүй талбаруудыг бодит мэдээллээр солино:

1. Хоёр гишүүний нэр ба GitHub нэр.
2. Хоёр feature commit SHA ба холбоос.
3. Хоёр PR холбоос.
4. PR бүр дээрх нөгөө хүний хамгийн багадаа 2 comment-ийн **тус бүрийн permalink**.
5. Conflict-ийн screenshot, шийдлийн merge commit SHA ба холбоос.
6. PR-үүд main руу merge болсон commit-ууд.
7. Эцсийн main дээр 18 тест OK болсон гаралт/зураг.

GitHub comment-ийн `… → Copy link` ашиглан тухайн comment-ийн холбоосыг авна. PR-ийн ерөнхий холбоосыг comment-ийн оронд давтан тавихгүй. `git log`-ийн гарсан жинхэнэ SHA-г ашиглана, жишээ SHA зохиохгүй.

Биелсэн шалгуурыг л `lab6/README.md` дээр `[x]` болгоно. Дараа нь тайлангаа main дээр commit/push хийнэ (main хамгаалалттай бол тайлангийн тусдаа PR ашиглана):

```powershell
git add lab6/README.md lab6/evidence
git diff --cached --stat
git commit -m "Record Lab 6 PR, review and merge-conflict evidence"
git push origin main
```

Багшид илгээх гол холбоос:

https://github.com/Buyka1108/intercity-transport-delivery

Тайлбартаа `lab6/README.md` болон `lab6/evidence/report.md`-д нотолгоо байгаа гэж заана. Token, нууц үг, хувийн мэдээлэлтэй screenshot бүү нэм.
