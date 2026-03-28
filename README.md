# 💎 جوهرة تعز | Jawhara Grand ERP

**نظام محاسبي متكامل لإدارة المجمعات التجارية والشركات**  
An integrated accounting and management system for malls and businesses.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

---

## 📌 Description | وصف المشروع

Jawhara Grand ERP is a complete desktop application designed to manage all aspects of a business, with a focus on malls and shopping centers. It handles **tenant management, utility services (electricity/water) readings, cash boxes, receipts, expenses, HR, payroll, double‑entry accounting, financial reports, and automated backups**. The system is built with Python and uses a modern GUI (`ttkbootstrap`), SQLite for data persistence, and supports Arabic language throughout.

**نظام جوهرة تعز** هو تطبيق متكامل لإدارة الأعمال، يركز على إدارة المجمعات التجارية. يتضمن إدارة المستأجرين، قراءات الخدمات (كهرباء/ماء)، الصناديق النقدية، سندات القبض والصرف، الموارد البشرية والرواتب، محاسبة القيد المزدوج، التقارير المالية، والنسخ الاحتياطي التلقائي. الواجهة مصممة بالعربية وتدعم اللغة العربية بالكامل.

---

## ✨ Features | الميزات

### Core Modules | الوحدات الرئيسية
- **Tenants Management** – Add, edit, delete tenants; manage rent, contract dates, and balances.
- **Services & Readings** – Manage electricity/water tariffs, record meter readings, calculate consumption and bills.
- **Cash Boxes** – Multiple cash boxes with opening balances, minimum balance alerts.
- **Receipts (Income) & Vouchers (Expenses)** – Professional PDF receipts, double‑entry accounting integration.
- **HR & Payroll** – Employees, departments, salary slips with allowances/deductions.
- **Accounting** – Chart of accounts, journal entries, trial balance, income statement, balance sheet, period closing.
- **Reports** – PDF and Excel reports for tenants, dues, cash movement, readings, and more.
- **Automated Backup** – Scheduled daily backups with automatic cleanup.
- **Alerts** – Reminders for readings, expiring contracts, and low cash balances.
- **Multi‑language Support** – Full Arabic UI and Arabic‑enabled PDF output (optional libraries).

---

## 🛠️ Technologies Used | التقنيات المستخدمة

- **Python 3.8+**
- **ttkbootstrap** – Modern themed widgets
- **SQLite** – Lightweight embedded database
- **Pandas** – Excel import/export
- **Matplotlib** – Dashboard charts
- **FPDF** – PDF generation with custom Arabic fonts
- **arabic_reshaper & python-bidi** – Arabic text rendering (optional)

---

## 🚀 Installation | التثبيت

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/jawhara-grand-erp.git
   cd jawhara-grand-erp
