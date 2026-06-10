with source as (
    select * from {{source('ecommerce_v2','raw_users')}}
),
renamed as (
        select
            id as user_id,
            email as user_email,
            username,
            firstname as first_name,
            lastname as last_name,
            city,
            zipcode,
            phone
        from source
)
select * from renamed