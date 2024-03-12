# Generated by Django 5.0.2 on 2024-03-07 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('marital_status', models.CharField(max_length=20)),
                ('nationality_id', models.PositiveIntegerField()),
                ('citizenship_id', models.PositiveIntegerField()),
                ('ssn', models.CharField(max_length=20)),
                ('employee_email', models.EmailField(max_length=254)),
                ('personal_email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('emergency_contact_name', models.CharField(max_length=100)),
                ('emergency_contact_number', models.CharField(max_length=20)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=20)),
                ('employment_type_id', models.PositiveIntegerField()),
                ('employment_type', models.CharField(max_length=50)),
                ('employment_status_id', models.PositiveIntegerField()),
                ('employment_status', models.CharField(max_length=50)),
                ('hire_date', models.DateField()),
                ('termination_date', models.DateField(blank=True, null=True)),
                ('department_id', models.PositiveIntegerField()),
                ('department_name', models.CharField(max_length=50)),
                ('job_title_id', models.PositiveIntegerField()),
                ('job_title', models.CharField(max_length=50)),
                ('pay_grade_id', models.PositiveIntegerField()),
                ('pay_grade', models.CharField(max_length=50)),
                ('base_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hourly_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('commission_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bonus_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('benefits_eligibility_date', models.DateField()),
                ('vacation_days', models.PositiveIntegerField()),
                ('sick_days', models.PositiveIntegerField()),
                ('employee_photo', models.ImageField(blank=True, null=True, upload_to='employee_photos/')),
                ('employee_signature', models.ImageField(blank=True, null=True, upload_to='employee_signatures/')),
                ('employee_resume_id', models.PositiveIntegerField(blank=True, null=True)),
                ('education_level', models.CharField(max_length=50)),
                ('university_id', models.PositiveIntegerField(blank=True, null=True)),
                ('university_name', models.CharField(blank=True, max_length=100, null=True)),
                ('major_subject', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_year', models.PositiveIntegerField(blank=True, null=True)),
                ('professional_certificates', models.TextField(blank=True, null=True)),
                ('skill_set', models.TextField(blank=True, null=True)),
                ('languages_spoken', models.TextField(blank=True, null=True)),
                ('work_experience', models.TextField(blank=True, null=True)),
                ('current_contract_id', models.PositiveIntegerField(blank=True, null=True)),
                ('contract_start_date', models.DateField(blank=True, null=True)),
                ('contract_end_date', models.DateField(blank=True, null=True)),
                ('probation_period_end', models.DateField(blank=True, null=True)),
                ('performance_review_date', models.DateField(blank=True, null=True)),
                ('promotion_eligibility_date', models.DateField(blank=True, null=True)),
                ('emergency_contacts', models.TextField(blank=True, null=True)),
                ('work_permit_id', models.PositiveIntegerField(blank=True, null=True)),
                ('work_permit_expiry_date', models.DateField(blank=True, null=True)),
                ('tax_regime', models.CharField(blank=True, max_length=50, null=True)),
                ('tax_file_number', models.CharField(blank=True, max_length=20, null=True)),
                ('payroll_schedule', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=50, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_members', to='base.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('marital_status', models.CharField(max_length=20)),
                ('nationality_id', models.PositiveIntegerField()),
                ('citizenship_id', models.PositiveIntegerField()),
                ('ssn', models.CharField(max_length=20)),
                ('customer_email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=20)),
                ('customer_type', models.CharField(max_length=50)),
                ('customer_segment', models.CharField(max_length=50)),
                ('customer_source', models.CharField(max_length=50)),
                ('customer_status', models.CharField(max_length=50)),
                ('customer_since', models.DateField()),
                ('last_purchase_date', models.DateField(blank=True, null=True)),
                ('total_purchases', models.PositiveIntegerField(default=0)),
                ('total_spent', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('average_order_value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('average_order_frequency', models.PositiveIntegerField(default=0)),
                ('customer_preferences', models.TextField(blank=True, null=True)),
                ('customer_interests', models.TextField(blank=True, null=True)),
                ('customer_feedback', models.TextField(blank=True, null=True)),
                ('customer_complaints', models.TextField(blank=True, null=True)),
                ('customer_resolution', models.TextField(blank=True, null=True)),
                ('customer_loyalty_program', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_loyalty_points', models.PositiveIntegerField(default=0)),
                ('customer_loyalty_tier', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_discounts', models.TextField(blank=True, null=True)),
                ('customer_rewards', models.TextField(blank=True, null=True)),
                ('customer_notes', models.TextField(blank=True, null=True)),
                ('customer_photo', models.ImageField(blank=True, null=True, upload_to='customer_photos/')),
                ('customer_signature', models.ImageField(blank=True, null=True, upload_to='customer_signatures/')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('company_website', models.URLField(blank=True, null=True)),
                ('company_industry', models.CharField(blank=True, max_length=50, null=True)),
                ('company_size', models.PositiveIntegerField(blank=True, null=True)),
                ('company_revenue', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('company_employees', models.PositiveIntegerField(blank=True, null=True)),
                ('billing_address_line1', models.CharField(max_length=100)),
                ('billing_address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_city', models.CharField(max_length=50)),
                ('billing_state', models.CharField(max_length=50)),
                ('billing_country', models.CharField(max_length=50)),
                ('billing_zip_code', models.CharField(max_length=20)),
                ('shipping_address_line1', models.CharField(max_length=100)),
                ('shipping_address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_city', models.CharField(max_length=50)),
                ('shipping_state', models.CharField(max_length=50)),
                ('shipping_country', models.CharField(max_length=50)),
                ('shipping_zip_code', models.CharField(max_length=20)),
                ('payment_method_id', models.PositiveIntegerField()),
                ('payment_method_name', models.CharField(max_length=50)),
                ('credit_card_number', models.CharField(blank=True, max_length=20, null=True)),
                ('credit_card_expiry', models.DateField(blank=True, null=True)),
                ('credit_card_cvv', models.PositiveIntegerField(blank=True, null=True)),
                ('credit_card_type', models.CharField(blank=True, max_length=20, null=True)),
                ('contact_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_contacts', to='base.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.TextField()),
                ('category_id', models.PositiveIntegerField()),
                ('category_name', models.CharField(max_length=50)),
                ('brand_id', models.PositiveIntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_dimensions', models.CharField(max_length=50)),
                ('units_in_stock', models.PositiveIntegerField()),
                ('units_on_order', models.PositiveIntegerField()),
                ('reorder_level', models.PositiveIntegerField()),
                ('discontinued', models.BooleanField(default=False)),
                ('discontinued_date', models.DateField(blank=True, null=True)),
                ('supplier_id', models.PositiveIntegerField()),
                ('supplier_name', models.CharField(max_length=100)),
                ('manufacturer_id', models.PositiveIntegerField()),
                ('manufacturer_name', models.CharField(max_length=100)),
                ('country_of_origin', models.CharField(max_length=50)),
                ('production_date', models.DateField()),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('shelf_life', models.PositiveIntegerField()),
                ('warranty_period', models.PositiveIntegerField()),
                ('warranty_terms', models.TextField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('product_specifications', models.TextField()),
                ('product_features', models.TextField()),
                ('product_options', models.TextField(blank=True, null=True)),
                ('product_variants', models.TextField(blank=True, null=True)),
                ('size_id', models.PositiveIntegerField()),
                ('size_name', models.CharField(max_length=50)),
                ('material_id', models.PositiveIntegerField()),
                ('material_name', models.CharField(max_length=50)),
                ('production_lead_time', models.PositiveIntegerField()),
                ('production_batch_size', models.PositiveIntegerField()),
                ('production_notes', models.TextField(blank=True, null=True)),
                ('quality_control_procedures', models.TextField()),
                ('quality_control_notes', models.TextField(blank=True, null=True)),
                ('packaging_type', models.CharField(max_length=50)),
                ('packaging_materials', models.TextField()),
                ('packaging_instructions', models.TextField()),
                ('shipping_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_dimensions', models.CharField(max_length=50)),
                ('shipping_instructions', models.TextField()),
                ('storage_requirements', models.TextField()),
                ('storage_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('storage_humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('handling_instructions', models.TextField()),
                ('safety_instructions', models.TextField()),
                ('disposal_instructions', models.TextField()),
                ('product_certifications', models.TextField(blank=True, null=True)),
                ('product_compliance', models.TextField(blank=True, null=True)),
                ('product_documentation', models.TextField(blank=True, null=True)),
                ('product_manuals', models.TextField(blank=True, null=True)),
                ('product_videos', models.TextField(blank=True, null=True)),
                ('product_faqs', models.TextField(blank=True, null=True)),
                ('product_reviews', models.TextField(blank=True, null=True)),
                ('product_ratings', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('product_popularity', models.PositiveIntegerField(blank=True, null=True)),
                ('product_trends', models.TextField(blank=True, null=True)),
                ('product_seasonality', models.TextField(blank=True, null=True)),
                ('product_lifecycle', models.CharField(blank=True, max_length=50, null=True)),
                ('product_roadmap', models.TextField(blank=True, null=True)),
                ('product_retirement_date', models.DateField(blank=True, null=True)),
                ('product_successor', models.CharField(blank=True, max_length=100, null=True)),
                ('product_notes', models.TextField(blank=True, null=True)),
                ('supervising_employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervised_products', to='base.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('order_number', models.CharField(max_length=20)),
                ('order_status', models.CharField(max_length=50)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_tax', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_shipping_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_shipping_method', models.CharField(max_length=50)),
                ('order_tracking_number', models.CharField(blank=True, max_length=50, null=True)),
                ('order_ship_date', models.DateField(blank=True, null=True)),
                ('order_delivery_date', models.DateField(blank=True, null=True)),
                ('order_billing_address_line1', models.CharField(max_length=100)),
                ('order_billing_address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('order_billing_city', models.CharField(max_length=50)),
                ('order_billing_state', models.CharField(max_length=50)),
                ('order_billing_country', models.CharField(max_length=50)),
                ('order_billing_zip_code', models.CharField(max_length=20)),
                ('order_shipping_address_line1', models.CharField(max_length=100)),
                ('order_shipping_address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('order_shipping_city', models.CharField(max_length=50)),
                ('order_shipping_state', models.CharField(max_length=50)),
                ('order_shipping_country', models.CharField(max_length=50)),
                ('order_shipping_zip_code', models.CharField(max_length=20)),
                ('payment_method_id', models.PositiveIntegerField()),
                ('payment_method_name', models.CharField(max_length=50)),
                ('payment_transaction_id', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(max_length=50)),
                ('sales_commission', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('sales_notes', models.TextField(blank=True, null=True)),
                ('product_name', models.CharField(max_length=100)),
                ('product_quantity', models.PositiveIntegerField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('product_tax', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('product_shipping_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('product_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('line_item_notes', models.TextField(blank=True, null=True)),
                ('return_request_id', models.PositiveIntegerField(blank=True, null=True)),
                ('return_reason', models.TextField(blank=True, null=True)),
                ('return_status', models.CharField(blank=True, max_length=50, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('return_quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('return_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('return_notes', models.TextField(blank=True, null=True)),
                ('refund_id', models.PositiveIntegerField(blank=True, null=True)),
                ('refund_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('refund_date', models.DateField(blank=True, null=True)),
                ('refund_notes', models.TextField(blank=True, null=True)),
                ('exchange_id', models.PositiveIntegerField(blank=True, null=True)),
                ('exchange_quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('exchange_notes', models.TextField(blank=True, null=True)),
                ('cancelation_request_id', models.PositiveIntegerField(blank=True, null=True)),
                ('cancelation_reason', models.TextField(blank=True, null=True)),
                ('cancelation_status', models.CharField(blank=True, max_length=50, null=True)),
                ('cancelation_date', models.DateField(blank=True, null=True)),
                ('cancelation_notes', models.TextField(blank=True, null=True)),
                ('promotion_id', models.PositiveIntegerField(blank=True, null=True)),
                ('promotion_name', models.CharField(blank=True, max_length=100, null=True)),
                ('promotion_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('promotion_notes', models.TextField(blank=True, null=True)),
                ('additional_notes', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='base.customer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales', to='base.product')),
                ('sales_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales', to='base.employee')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_sales',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='base.sale'),
        ),
    ]