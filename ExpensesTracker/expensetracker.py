import json
import os
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich import box

console = Console()
FILE_NAME = "expenses.json"


# ---------------- DATA FUNCTIONS ---------------- #

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# ---------------- CALCULATIONS ---------------- #

def get_summary(data):
    income = sum(item["amount"] for item in data if item["type"] == "Income")
    expense = sum(item["amount"] for item in data if item["type"] == "Expense")
    balance = income - expense
    return income, expense, balance


# ---------------- UI FUNCTIONS ---------------- #

def show_header():
    console.clear()

    console.print(
        Panel(
            "[bold cyan]💰 EXPENSE TRACKER PRO[/bold cyan]\n"
            "[dim]Track • Analyze • Control Your Money[/dim]",
            border_style="bright_blue",
            padding=(1, 10),
        )
    )


def show_dashboard(data):
    income, expense, balance = get_summary(data)

    table = Table(
        title="📊 Financial Overview",
        box=box.ROUNDED,
        border_style="cyan",
        show_header=True
    )

    table.add_column("Income", justify="center", style="green")
    table.add_column("Expenses", justify="center", style="red")
    table.add_column("Balance", justify="center", style="yellow")

    table.add_row(
        f"₹ {income:,.2f}",
        f"₹ {expense:,.2f}",
        f"₹ {balance:,.2f}"
    )

    console.print(table)


# ---------------- ADD TRANSACTION ---------------- #

def add_transaction(data):

    console.print("\n[bold cyan]➕ Add New Transaction[/bold cyan]\n")

    transaction_type = Prompt.ask(
        "Transaction Type",
        choices=["Income", "Expense"],
        default="Expense"
    )

    category = Prompt.ask(
        "Category",
        default="General"
    )

    description = Prompt.ask(
        "Description",
        default="No description"
    )

    while True:
        try:
            amount = float(Prompt.ask("Amount (₹)"))
            if amount <= 0:
                console.print("[red]Amount must be greater than zero![/red]")
                continue
            break
        except ValueError:
            console.print("[red]Please enter a valid number![/red]")

    transaction = {
        "id": len(data) + 1,
        "type": transaction_type,
        "category": category.title(),
        "description": description,
        "amount": amount,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    data.append(transaction)
    save_data(data)

    console.print("\n[bold green]✓ Transaction added successfully![/bold green]")


# ---------------- VIEW TRANSACTIONS ---------------- #

def view_transactions(data):

    if not data:
        console.print("\n[yellow]No transactions found![/yellow]")
        return

    table = Table(
        title="📋 Transaction History",
        box=box.ROUNDED,
        border_style="bright_blue"
    )

    table.add_column("ID", justify="center")
    table.add_column("Type", justify="center")
    table.add_column("Category")
    table.add_column("Description")
    table.add_column("Amount", justify="right")
    table.add_column("Date")

    for item in data:

        color = "green" if item["type"] == "Income" else "red"

        table.add_row(
            str(item["id"]),
            f"[{color}]{item['type']}[/{color}]",
            item["category"],
            item["description"],
            f"₹ {item['amount']:,.2f}",
            item["date"]
        )

    console.print(table)


# ---------------- EXPENSE ANALYTICS ---------------- #

def expense_analysis(data):

    expenses = [item for item in data if item["type"] == "Expense"]

    if not expenses:
        console.print("\n[yellow]No expenses available for analysis![/yellow]")
        return

    categories = {}

    for item in expenses:
        category = item["category"]
        categories[category] = categories.get(category, 0) + item["amount"]

    table = Table(
        title="📊 Expense Analysis by Category",
        box=box.ROUNDED,
        border_style="magenta"
    )

    table.add_column("Category", style="cyan")
    table.add_column("Amount", justify="right", style="red")

    for category, amount in sorted(
        categories.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        table.add_row(category, f"₹ {amount:,.2f}")

    console.print(table)


# ---------------- DELETE TRANSACTION ---------------- #

def delete_transaction(data):

    if not data:
        console.print("\n[yellow]No transactions available![/yellow]")
        return

    view_transactions(data)

    try:
        transaction_id = int(
            Prompt.ask("\nEnter Transaction ID to delete")
        )

        transaction = next(
            (item for item in data if item["id"] == transaction_id),
            None
        )

        if transaction:

            if Confirm.ask(
                f"Delete transaction '{transaction['description']}'?"
            ):
                data.remove(transaction)
                save_data(data)

                console.print(
                    "[bold green]✓ Transaction deleted successfully![/bold green]"
                )
        else:
            console.print("[red]Transaction ID not found![/red]")

    except ValueError:
        console.print("[red]Please enter a valid ID![/red]")


# ---------------- MAIN PROGRAM ---------------- #

def main():

    data = load_data()

    while True:

        show_header()
        show_dashboard(data)

        console.print(
            """
[bold cyan]
[1][/bold cyan] ➕ Add Transaction
[bold cyan][2][/bold cyan] 📋 View Transactions
[bold cyan][3][/bold cyan] 📊 Expense Analytics
[bold cyan][4][/bold cyan] 🗑️ Delete Transaction
[bold cyan][5][/bold cyan] 🚪 Exit
"""
        )

        choice = Prompt.ask(
            "[bold yellow]Select an option[/bold yellow]",
            choices=["1", "2", "3", "4", "5"]
        )

        console.print()

        if choice == "1":
            add_transaction(data)

        elif choice == "2":
            view_transactions(data)

        elif choice == "3":
            expense_analysis(data)

        elif choice == "4":
            delete_transaction(data)

        elif choice == "5":
            console.print(
                Panel(
                    "[bold green]Thank you for using Expense Tracker Pro! 💰[/bold green]\n"
                    "[dim]Keep tracking. Keep growing.[/dim]",
                    border_style="green"
                )
            )
            break

        Prompt.ask(
            "\n[dim]Press Enter to return to dashboard[/dim]",
            default=""
        )


if __name__ == "__main__":
    main()
