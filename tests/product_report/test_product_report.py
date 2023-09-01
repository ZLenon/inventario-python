# Requisito 2
from inventory_report.product import Product


def test_product_report() -> None:
    pdt = Product(
        "33",
        "Tapioca",
        "Yoki",
        "04/06/2001",
        "04/06/2002",
        "tap-04062002",
        """Preaqueça a frigideira, de preferência antiaderente.
Com uma colher, polvilhe a tapioca na frigideira preenchendo toda sua
 superfície com a goma. Passe a colher sobre a tapioca para que um lado
não fique maior que o outro, tornando-a plana e uniforme.
Aqueça na frigideira por cerca de 5 minutos.
Depois, basta acrescentar o recheio e enrolá-la.""",
    )

    mock = str(pdt)

    result_class_product = (
        f"The product {pdt.id} - {pdt.product_name} "
        f"with serial number {pdt.serial_number} "
        f"manufactured on {pdt.manufacturing_date} "
        f"by the company {pdt.company_name} "
        f"valid until {pdt.expiration_date} "
        "must be stored according to the following instructions: "
        f"{pdt.storage_instructions}."
    )

    assert mock == result_class_product
