# درس کلاس گیت نوجوان سه‌شنبه

## از مخزن خالی تا درخت فرکتال

در این درس یک مخزن شخصی می‌سازی و فرکتال را از خط اول می‌نویسی. یک‌بار کد پایه را روی `main` می‌فرستی. بعد، تغییر رنگ و شکوفه‌ها را هرکدام با یک شاخه و یک Pull Request به `main` اضافه می‌کنی.

### ۱. مخزن شخصی خودت را در GitHub بساز

- با حساب خودت وارد GitHub شو. از منوی `+`، گزینهٔ **New repository** را بزن.
- مالک را حساب خودت بگذار. مخزن را `fractal-lab` و وضعیتش را **Private** انتخاب کن.
- گزینه‌های README، `.gitignore` و License را غیرفعال بگذار و **Create repository** را بزن.
- از **Quick setup → HTTPS** نشانی مخزن خودت را کپی کن. در یک پوشهٔ مناسب روی کامپیوتر Git Bash را باز کن و فرمان زیر را بزن. اول `YOUR-USERNAME` را با نام حساب خودت عوض کن.

```bash
git clone https://github.com/YOUR-USERNAME/fractal-lab.git
cd fractal-lab
git remote -v
```

> **خروجی مورد انتظار**
>
> برای مخزن خالی، هشدار `You appear to have cloned an empty repository` طبیعی است. `git clone` خودش مقصد `origin` را ثبت می‌کند. `git remote -v` باید نشانی مخزن شخصی تو را برای `fetch` و `push` نشان بدهد.

ریپوی کلاس را برای خواندن درس باز کن. تمرین، شاخه‌ها و Pull Requestهای خودت را در مخزنی که با حساب خودت ساختی انجام بده.

## درخت سفید را در Thonny بساز

### ۲. فایل main.py را بنویس

در Thonny یک فایل تازه بساز. آن را دقیقاً با نام `main.py` داخل پوشهٔ `fractal-lab` ذخیره کن. چهار فاصلهٔ ابتدای خط‌های داخل تابع را رعایت کن.

```python
import turtle

screen = turtle.Screen()
screen.setup(800, 650)
screen.title("Fractal Lab")
screen.bgcolor("#101426")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.pensize(2)

tips = []


def branch(size):
    if size < 16:
        tips.append(pen.pos())
        return
    pen.forward(size)
    pen.left(28)
    branch(size * 0.7)
    pen.right(56)
    branch(size * 0.7)
    pen.left(28)
    pen.backward(size)


pen.penup()
pen.goto(0, -260)
pen.setheading(90)
pen.pendown()
branch(110)

# Add decorations here in feature/decor

screen.update()
screen.mainloop()
```

> **خروجی مورد انتظار**
>
> با F5 باید یک درخت سفید روی زمینهٔ سرمه‌ای ببینی. با هر شاخهٔ کوچک، `branch` خودش را روی اندازه‌ای کوچک‌تر صدا می‌زند. `tips` جای نوک شاخه‌ها را برای مرحلهٔ شکوفه نگه می‌دارد.

## README و اولین پوش روی main

### ۳. راهنمای پروژه را بساز

در Git Bash، `notepad README.md` را اجرا کن. اگر Notepad پیشنهاد ساخت فایل داد، تأیید کن. متن زیر را بنویس و ذخیره کن. اسم فایل در پوشه باید `README.md` باشد.

```markdown
# Fractal Lab

A fractal tree made with Python Turtle.

## How to run

Open `main.py` in Thonny and press F5.
```

### ۴. اولین کامیت را در Git ثبت کن

پنجرهٔ فرکتال را ببند. در Git Bash همان پوشه فرمان‌ها را یکی‌یکی اجرا کن. اگر کامیت خطا داد، قبل از پوش دلیل خطا را بررسی کن.

```bash
git status --short
git add main.py README.md
git commit -m "Create white fractal tree and README"
git branch -M main
git push -u origin main
```

اگر Git نام و ایمیل خواست، هویت همین مخزن را با تنظیم محلی وارد کن و دوباره `git commit` را بزن. اگر برای پوش مرورگر باز شد، با حسابِ صاحب مخزن وارد شو.

```bash
git config user.name "YOUR NAME"
git config user.email "YOUR_EMAIL"
```

> **خروجی مورد انتظار**
>
> بعد از پوش، صفحهٔ **Code** مخزن را تازه کن. روی `main` باید `main.py` و `README.md` را ببینی و عنوان **Fractal Lab** پایین فهرست فایل‌ها نمایش داده شود. این پوش پایهٔ مشترک برای دو Pull Request است.

`origin` نام کوتاه مقصد HTTPS است. `-u` شاخهٔ محلی را به شاخهٔ متناظر در GitHub وصل می‌کند.

## رنگ تازه روی یک شاخهٔ تازه

### ۵. شاخهٔ تغییر رنگ را بساز

اول با `git status` مطمئن شو روی `main` هستی و تغییر ثبت‌نشده نداری. بعد شاخهٔ رنگ را بساز.

```bash
git switch -c feature/colors
git branch --show-current
```

> **خروجی مورد انتظار**
>
> خروجی باید `feature/colors` باشد. شاخهٔ `main` همچنان وجود دارد و با `git branch` می‌توانی هر دو شاخه را ببینی.

### ۶. فقط این دو خط را در main.py جایگزین کن

```diff
-screen.bgcolor("#101426")
+screen.bgcolor("#1a1035")

-pen.color("white")
+pen.color("#65dcff")
```

نشانه‌های `+` و `-` برای نمایش تغییرند. آن‌ها را در پایتون تایپ نکن. فایل را ذخیره کن و با F5 اجرا کن.

> **خروجی مورد انتظار**
>
> درخت آبی روشن و زمینه بنفش تیره است. پس از `git diff -- main.py` باید تغییر همان دو خط را ببینی.

### ۷. شاخهٔ رنگ را کامیت و پوش کن

```bash
git diff -- main.py
git add main.py
git commit -m "Add neon tree colors"
git push -u origin feature/colors
```

> **خروجی مورد انتظار**
>
> شاخهٔ `feature/colors` در GitHub دیده می‌شود. اگر در مرورگر روی `main` بمانی، هنوز کد درخت سفید را می‌بینی. صفحهٔ بعد تغییر رنگ را با PR به `main` می‌رساند.

## Pull Request رنگ را بساز و ادغام کن

### ۸. تغییر پیشنهادی را در GitHub باز کن

در مخزن شخصی‌ات روی **Compare & pull request** بزن. اگر دکمه را ندیدی، **Pull requests → New pull request** را باز کن. در **base** شاخهٔ مقصد `main` و در **compare** شاخهٔ `feature/colors` را انتخاب کن.

> **خروجی مورد انتظار**
>
> در **Files changed** باید فقط `main.py` را ببینی و همان دو خط رنگ فرق داشته باشند. اگر فایل اضافه یا شاخهٔ دیگری می‌بینی، قبل از ساخت PR انتخاب‌ها را بررسی کن.

**عنوان آماده**

رنگ درخت و پس‌زمینه را تغییر می‌دهد

**متن آماده**

```markdown
## تغییرها
- پس‌زمینه را بنفش تیره کردم.
- رنگ قلم درخت را آبی روشن کردم.

## بررسی در Thonny
- `main.py` را با F5 اجرا کردم و درخت آبی را روی زمینهٔ بنفش دیدم.
- در Files changed بررسی کردم که فقط دو خط رنگ در `main.py` تغییر کرده‌اند.
```

### ۹. در GitHub ادغام کن و main محلی را به‌روز کن

عنوان و متن بالا را وارد کن و **Create pull request** را بزن. بعد از بررسی تغییرها و طبق هماهنگی مربی، **Merge pull request → Confirm merge** را بزن. صفحه باید وضعیت **Merged** نشان بدهد. در Git Bash بزن:

```bash
git switch main
git pull --ff-only
git status
```

> **خروجی مورد انتظار**
>
> `git status` نشان می‌دهد روی `main` هستی. در Thonny `main.py` را دوباره از دیسک باز کن و F5 بزن. حالا درخت رنگی روی `main` هم اجرا می‌شود.

## شکوفه‌های قابل کلیک را بنویس

### ۱۰. از main رنگی شاخهٔ گل‌ها را بساز

اول مطمئن شو `main` پس از PR رنگ به‌روز است و تغییر ناتمام نداری. سپس شاخهٔ تازه را از همان `main` بساز.

```bash
git switch -c feature/decor
git branch --show-current
```

در Thonny یک فایل جدید به نام `decor.py` کنار `main.py` بساز و این کد را بنویس:

```python
def decorate(screen, pen, tips):
    pen.penup()

    def flower(x, y):
        for dx, dy in [(-8, 0), (8, 0), (0, -8), (0, 8)]:
            pen.goto(x + dx, y + dy)
            pen.dot(11, "#ff70b8")
        pen.goto(x, y)
        pen.dot(8, "#ffe16a")
        screen.update()

    for x, y in tips:
        flower(x, y)

    screen.onclick(flower)
```

### ۱۱. تابع را درست بعد از رسم درخت صدا بزن

در `main.py` جزوه، کامنت خط ۳۷ را با `import` در خط ۳۷ و فراخوانی در خط ۳۸ عوض کن. هر دو از ابتدای سطرند. اگر شماره‌ها فرق دارند، بین `branch(110)` و `screen.update()` را پیدا کن. علامت‌های `+` و `-` را تایپ نکن.

```diff
 branch(110)

-# Add decorations here in feature/decor
+from decor import decorate
+decorate(screen, pen, tips)

 screen.update()
 screen.mainloop()
```

> **خروجی مورد انتظار**
>
> هر دو فایل را ذخیره کن و فقط `main.py` را با F5 اجرا کن. نوک شاخه‌ها گل صورتی با مرکز زرد دارند. با هر کلیک چپ داخل پنجره، یک گل تازه در همان نقطه اضافه می‌شود.

## Pull Request شکوفه‌ها را بفرست

### ۱۲. دو فایل را ثبت کن و شاخه را بفرست

```bash
git status --short
git add main.py decor.py
git commit -m "Add blossoms and mouse clicks"
git push -u origin feature/decor
```

اگر `__pycache__/` هم در وضعیت دیده شد، آن را به کامیت اضافه نکن.

### ۱۳. PR دوم را در مخزن خودت باز کن

از **Pull requests → New pull request** شروع کن. **base** را `main` و **compare** را `feature/decor` بگذار. **Create pull request** را بزن تا فرم باز شود. عنوان و متن زیر را وارد کن و دوباره همان دکمه را بزن.

> **خروجی مورد انتظار**
>
> در **Files changed** باید `decor.py` به‌عنوان فایل تازه و `main.py` با تغییر محل فراخوانی دیده شوند. تغییر رنگ در PR قبلی وارد `main` شده است.

**عنوان آماده**

شکوفه‌های قابل کلیک را اضافه می‌کند

**متن آماده**

```markdown
## تغییرها
- `decor.py` را برای رسم شکوفه روی نوک شاخه‌ها ساختم.
- در `main.py` بعد از رسم درخت، تابع `decorate` را فراخوانی کردم.

## بررسی در Thonny
- `main.py` را اجرا کردم و شکوفه‌های صورتی با مرکز زرد را دیدم.
- دو نقطهٔ جدا را با کلیک چپ امتحان کردم و هر بار یک شکوفه در همان نقطه ظاهر شد.
```

### ۱۴. پس از ادغام، نسخهٔ کامل را دوباره اجرا کن

پس از بررسی و تأیید مربی، **Merge pull request → Confirm merge** را بزن. بعد در Git Bash فرمان‌های زیر را بزن.

```bash
git switch main
git pull --ff-only
git status
```

> **خروجی مورد انتظار**
>
> روی `main` در GitHub باید `main.py`، `decor.py` و `README.md` را ببینی. بعد از بازکردن دوبارهٔ فایل در Thonny، رنگ آبی و گل‌های قابل کلیک با هم کار می‌کنند.

## بررسی پایانی پروژه

### سه چیز را در مخزن خودت پیدا کن

- فایل `README.md` و راهنمای اجرا در صفحهٔ **Code** شاخهٔ `main`.
- دو Pull Request با وضعیت **Merged**، یکی برای رنگ و یکی برای شکوفه‌ها.
- فرکتال رنگی و گل‌های قابل کلیک در اجرای `main.py` روی `main` محلی.

### اگر جایی گیر کردی

- اگر `origin` نام حساب دیگری را دارد، پوش نکن. خروجی `git remote -v` را با نشانی مخزن شخصی‌ات مقایسه کن.
- اگر **New pull request** چیزی برای مقایسه ندارد، با `git branch --show-current`، `git status` و آخرین پیام پوش بررسی کن شاخهٔ درست پوش شده باشد. در GitHub هم **base** و **compare** را چک کن.
- اگر `git pull --ff-only` یا ادغام خطا داد، با `git status` و متن کامل پیام به مربی نشان بده کجا متوقف شده‌ای. از `--force` استفاده نکن.
- اگر Thonny هنوز نسخهٔ قبلی را باز دارد، پس از اطمینان از ذخیرهٔ تغییرها فایل را ببند و دوباره از همان پوشه باز کن.
- اگر هنوز حساب آماده نداری یا شرایط سنی ساخت حساب را نداری، مراحل GitHub را روی نمایش مربی دنبال کن و کد را روی کامپیوترت بنویس.

### بلیط خروج

۱. در PR رنگ، base و compare چه شاخه‌هایی بودند؟

________________________

۲. چرا پس از ادغام در سایت، در Git Bash دوباره `git pull --ff-only` زدیم؟

________________________

## منابع رسمی GitHub

- [کلون با HTTPS](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- [شروع سریع Pull Request](https://docs.github.com/en/pull-requests/get-started/pull-request-quickstart)
- [گرفتن تغییرها از مخزن آنلاین](https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository)
