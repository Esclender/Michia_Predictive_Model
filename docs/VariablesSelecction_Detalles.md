El dataset **marketing\_campaign.csv** trata sobre una **campaña de marketing directo realizada por una empresa de productos minoristas**, y contiene información detallada de los clientes y su comportamiento de compra a lo largo de **2 años**.

| Columna | Traducción/Descripción |
| :---- | :---- |
| ID | Identificador único del cliente |
| **Datos demográficos del cliente** |  |
| Year\_Birth | Año de nacimiento del cliente |
| Education | Nivel educativo (ej. Graduation, PhD, etc.) |
| Marital\_Status | Estado civil (ej. Soltero, Casado, etc.) |
| Income | Ingreso anual en euros |
| Kidhome | Número de niños en el hogar |
| Teenhome | Número de adolescentes en el hogar |
| **Datos de comportamiento del cliente** |  |
| Dt\_Customer | Fecha de registro como cliente |
| Recency | Días desde la última compra |
| NumDealsPurchases | Número de compras con descuento |
| NumWebPurchases | Compras hechas por la web |
| NumCatalogPurchases | Compras por catálogo |
| NumStorePurchases | Compras en tienda |
| NumWebVisitsMonth | Visitas al sitio web en el último mes |
| **Gastos del cliente (últimos 2 años)** |  |
| MntWines | Gasto en vinos en los últimos 2 años |
| MntFruits | Gasto en frutas en los últimos 2 años |
| MntMeatProducts | Gasto en carne en los últimos 2 años |
| MntFishProducts | Gasto en pescado en los últimos 2 años |
| MntSweetProducts | Gasto en dulces en los últimos 2 años |
| MntGoldProds | Gasto en productos de oro en los últimos 2 años |
| **Respuesta a campañas de marketing** |  |
| AcceptedCmp1 | Aceptó campaña promocional 1 (1: sí, 0: no) |
| AcceptedCmp2 | Aceptó campaña promocional 2 |
| AcceptedCmp3 | Aceptó campaña promocional 3 |
| AcceptedCmp4 | Aceptó campaña promocional 4 |
| AcceptedCmp5 | Aceptó campaña promocional 5 |
| Complain | Se ha quejado en los últimos 2 años (1: sí) |
| **Variables constantes del sistema (sin valor predictivo)** |  |
| Z\_CostContact | Coste de contacto (valor constante) |
| Z\_Revenue | Ingreso general (valor constante) |
| Response | Aceptó la última campaña (objetivo: 1 \= sí, 0 \= no) |

**Objetivo**:

“Analicen las columnas. ¿Cuáles son útiles para predecir si un cliente comprará de nuevo? ¿Cuáles podrían confundir al modelo?”

**Cada equipo debe responder:**

* ¿Qué variables parecen irrelevantes o redundantes?

  ID: Es solo un identificador, no tiene valor predictivo.

* ¿Qué variables podrían ser útiles?

  Income: 	Los ingresos pueden estar relacionados con la capacidad de compra.

* ¿Qué relaciones lógicas pueden establecer?

Si un cliente tiene ingresos altos (Income) y gasta mucho en productos como vino o carne, probablemente es un cliente premium.

