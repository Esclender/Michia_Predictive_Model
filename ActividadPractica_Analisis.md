# Análisis Cualitativo del Dataset "marketing_campaign.csv"

## Variables Irrelevantes o Redundantes

- **ID**: Es solo un identificador único del cliente. No aporta información predictiva.
- **Variables constantes del sistema**:  
  - Z_CostContact  
  - Z_Revenue  
  Estas columnas tienen valores constantes y, por lo tanto, no contribuyen al poder predictivo del modelo.


## Variables Potencialmente Útiles

### Datos Demográficos
- **Year_Birth**: Permite calcular la edad, lo que puede relacionarse con el comportamiento de compra.  
- **Education**: El nivel educativo puede influir en el poder adquisitivo y preferencias de compra.
- **Marital_Status**: El estado civil podría estar relacionado con patrones familiares y decisiones de compra.
- **Income**: Es una variable clave, pues los ingresos están directamente asociados a la capacidad de compra y comportamiento de gasto.
- **Kidhome y Teenhome**: El número de niños y adolescentes en el hogar puede influir en las necesidades y consumo (especialmente de ciertos productos).

### Datos de Comportamiento y Gastos
- **Recency**: Los días desde la última compra pueden indicar el compromiso del cliente.  
- **NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth**: La frecuencia de compra y visitas, tanto en línea como en tienda, son indicadores del nivel de interacción y fidelidad.
- **Gastos en productos (MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds)**: Estos montos permiten segmentar a los clientes según sus preferencias y el nivel de gasto en distintas categorías.

### Respuesta a Campañas de Marketing
- **AcceptedCmp1 – AcceptedCmp5**: La aceptación previa de campañas promocionales es un fuerte indicativo de la predisposición del cliente a responder a futuras acciones.
- **Complain**: Si un cliente se ha quejado, podría estar relacionado con una experiencia negativa, lo que influiría en sus futuras decisiones de compra.

## Variables que Podrían Confundir al Modelo

- **Dt_Customer (sin procesamiento, formato no desestructurado)**: Tal como se registra, podría no ser informativo. Es recomendable transformarla a una variable de "antigüedad" o "tiempo como cliente (Podriamos realizar un casteo de rangos, llevar un mes con un año (abril 2021) seria al valor 1 (rango de tiempo 1))".
- **Variables de Gasto Altamente Correlacionadas**:  
   - Los diferentes montos de gasto (vino, frutas, carne, etc.) pueden estar correlacionados entre sí. Se debe evaluar la multicolinealidad para evitar redundancias.
- **Número de Campañas Aceptadas**:  
   - Si se suman o analizan de forma individual las variables AcceptedCmp1 a AcceptedCmp5, podríamos tener información muy similar o solapada. Es posible que una transformación (por ejemplo, contar el número total de campañas aceptadas) aporte mayor claridad.

## Relaciones Lógicas Potenciales

- Clientes con **altos ingresos** y mayor **gasto en productos premium** (por ejemplo, vinos o productos de oro) podrían pertenecer a la categoría "premium" y estar más dispuestos a aceptar nuevas campañas.
- Una **alta frecuencia de compras** (NumStorePurchases, NumWebPurchases, etc.) combinada con una **baja recency** suele indicar un cliente activo, con mayor predisposición a volver a comprar.
- Clientes que han aceptado varias campañas en el pasado (AcceptedCmp1-5) tienen una historia de respuesta positiva, lo que sugiere una probabilidad mayor de respuesta en futuras campañas.
- Un cliente con denuncias (Complain = 1) y bajos indicadores de gasto o frecuencia de compra podría ser menos receptivo a futuras campañas debido a experiencias negativas.

