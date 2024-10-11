from werkzeug.exceptions import NotFound
from app.database import MonthlyFee, MonthlyFees
from .forms import MonthlyFeeForm


def create(name: str, description: str, value: float) -> MonthlyFee:
    monthly_fee = MonthlyFee(name, description, value)
    MonthlyFee.save(monthly_fee)
    return monthly_fee


def get_all() -> MonthlyFees:
    return MonthlyFee.find_all()


def get_all_by_name(name: str) -> MonthlyFees:
    return MonthlyFee.find_all_by_name(name)


def get_one_by_id(id: int) -> MonthlyFee:
    monthly_fee = MonthlyFee.find_first_by_id(id)
    if not monthly_fee:
        raise NotFound('The monthly fee was not found.')
    return monthly_fee


def update(monthly_fee: MonthlyFee, form: MonthlyFeeForm) -> MonthlyFee:
    form.populate_obj(monthly_fee)
    MonthlyFee.save(monthly_fee)
    return monthly_fee


def delete(monthly_fee: MonthlyFee) -> None:
    MonthlyFee.delete(monthly_fee)
