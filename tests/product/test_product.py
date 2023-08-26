# Requisito 1
from inventory_report.product import Product


def test_create_product() -> None:
    produto = Product(
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
    assert produto.id == "33"
    assert produto.product_name == "Tapioca"
    assert produto.company_name == "Yoki"
    assert produto.manufacturing_date == "04/06/2001"
    assert produto.expiration_date == "04/06/2002"
    assert produto.serial_number == "tap-04062002"
    assert (
        produto.storage_instructions
        == """Preaqueça a frigideira, de preferência antiaderente.
Com uma colher, polvilhe a tapioca na frigideira preenchendo toda sua
 superfície com a goma. Passe a colher sobre a tapioca para que um lado
não fique maior que o outro, tornando-a plana e uniforme.
Aqueça na frigideira por cerca de 5 minutos.
Depois, basta acrescentar o recheio e enrolá-la."""
    )
