<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?size=38&duration=2500&pause=500&color=4F8CFF&center=true&vCenter=true&width=900&lines=Initializing+Reading+System...;Loading+Book+Manager...;System+Ready." />
</p>

> Not just a CRUD app.  
> A structured digital space to track, analyze and manage your reading universe.

---

## 🌌 Concept

Book Manager is designed as a minimal, dark, distraction-free reading dashboard.  
It combines structured data management with a clean SaaS-style interface.

This project explores:

- Secure authentication
- Permission-based workflows
- Data validation at multiple levels
- Aggregated statistics
- UI consistency and UX clarity

---

## 🧠 Why This Project?

Books are knowledge containers.  
This app treats them as structured data assets:

- Status tracking (Pending / Reading / Finished)
- Quantitative metrics (pages, ratings)
- Temporal validation (read date after published date)
- Author relationships (Many-to-Many)
- Visual representation (cover uploads)

It is a small-scale simulation of a real production system.

---

## 🏗 Architecture Overview

Layered design:

- **Models** → Business logic + validation
- **Forms** → User-level validation
- **Views** → Permission-based control
- **Templates** → Modern dark UI
- **Tests** → Reliability layer

---

## 🔐 Security Model

- Login required for detailed access
- Granular permissions:
  - add_book
  - change_book
  - delete_book
- CSRF protection
- Controlled POST-only logout (Django 5 compliant)

---

## 📊 Data Intelligence

The system provides real-time statistical insights:

- Maximum pages
- Minimum pages
- Average pages
- Average rating
- Status distribution
- Rating distribution

Built using Django ORM aggregations.

---

## 🧪 Reliability

Includes automated tests for:

- Model validation rules
- Form validation errors
- Permission enforcement
- View access control

Run:

```bash
python manage.py test
````

---

## 🖥 Interface Philosophy

Dark-mode first.
Minimal distractions.
Clean spacing.
Semantic structure.

Inspired by:

* Modern SaaS dashboards
* Knowledge management tools
* Clean developer UIs

---

## 🚀 Installation

Clone:

```bash
git clone https://github.com/Oumniya17/django-book-manager.git
cd django-book-manager
```

Install:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🧭 Roadmap

Future iterations may include:

* REST API version
* Dockerized environment
* User-specific libraries
* Public book sharing
* Advanced analytics dashboard

---

## 👩‍💻 Author

<p align="center">
  <img src="https://github.com/user-attachments/assets/d549c019-35bb-4af8-8e61-8d6885c6cd9b" width="200">
</p>

**Oumniya Chahidi — Developer & Designer**<br>

---

## ✨ Final Note

This project demonstrates structured backend thinking,
not just interface design.

It reflects:

* Clean architecture
* Validation-first mindset
* Permission-aware systems
* Professional UI discipline
