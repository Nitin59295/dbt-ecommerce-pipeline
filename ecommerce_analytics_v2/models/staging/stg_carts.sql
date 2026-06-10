with source as (
    select * from {{source('ecommerce_v2','raw_carts')}}
),
renamed as (
        select
            id as cart_id,
            user_id,
            date as order_date,
            product_id,
            quantity
        from source
)
select * from renamed