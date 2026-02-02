import pytest
from datetime import datetime
from database import get_session, get_engine, Employee, Company, Base


@pytest.fixture(scope="function")
def session():
    engine = get_engine()
    Base.metadata.create_all(engine)
    session = get_session()
    yield session
    session.close()


def test_add_employee(session):
    company = Company(name=f"Test Company "
                           f"{datetime.now().timestamp()}", is_active=True)
    session.add(company)
    session.commit()

    new_employee = Employee(
        first_name="Иван",
        last_name="Добавляемый",
        phone="+7-900-111-1111",
        company_id=company.id,
        is_active=True
    )
    session.add(new_employee)
    session.commit()

    retrieved = session.query(Employee).filter_by(
        first_name="Иван",
        last_name="Добавляемый"
    ).first()

    assert retrieved is not None
    assert retrieved.first_name == "Иван"

    session.delete(retrieved)
    session.delete(company)
    session.commit()


def test_update_employee(session):
    company = Company(name=f"Test Company "
                           f"{datetime.now().timestamp()}", is_active=True)
    session.add(company)
    session.commit()

    employee = Employee(
        first_name="Петр",
        last_name="Изменяемый",
        phone="+7-900-222-2222",
        company_id=company.id,
        is_active=True
    )
    session.add(employee)
    session.commit()

    employee_id = employee.id
    employee.first_name = "Петр Новый"
    employee.phone = "+7-900-333-3333"
    session.commit()

    updated = session.query(Employee).filter_by(id=employee_id).first()

    assert updated is not None
    assert updated.first_name == "Петр Новый"
    assert updated.phone == "+7-900-333-3333"

    session.delete(updated)
    session.delete(company)
    session.commit()


def test_delete_employee(session):
    company = Company(name=f"Test Company "
                           f"{datetime.now().timestamp()}", is_active=True)
    session.add(company)
    session.commit()

    employee = Employee(
        first_name="Удаляемый",
        last_name="Сотрудник",
        phone="+7-900-444-4444",
        company_id=company.id,
        is_active=True
    )
    session.add(employee)
    session.commit()

    employee_id = employee.id
    session.delete(employee)
    session.commit()

    deleted = session.query(Employee).filter_by(id=employee_id).first()

    assert deleted is None

    session.delete(company)
    session.commit()
