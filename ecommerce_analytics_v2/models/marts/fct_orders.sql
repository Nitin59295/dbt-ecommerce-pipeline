with products as (
        select * from {{ref('stg_products')}}
),
carts as (
    select * from {{ ref('stg_carts')}}
),

finally as (
        select
            p.product_category,
            sum(c.quantity * p.product_price) as total_revenue_per_category
            from products p join carts c
            on p.product_id = c.product_id
            group by p.product_category
)
select * from finally