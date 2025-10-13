CREATE TABLE "companies"(
    "id" UUID NOT NULL,
    "code_id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "category_id" UUID NOT NULL,
    "description" TEXT NULL,
    "province_id" UUID NULL,
    "district_id" UUID NULL,
    "subdistrict_id" UUID NULL,
    "ward_id" UUID NULL,
    "address" UUID NULL,
    "pic_name" TEXT NULL,
    "pic_contact" TEXT NULL,
    "note" TEXT NULL,
    "created_at" TIMESTAMP(0) WITH
        TIME zone NULL,
        "updated_at" TIMESTAMP(0)
    WITH
        TIME zone NULL
);
ALTER TABLE
    "companies" ADD PRIMARY KEY("id");
CREATE TABLE "company_categories"(
    "id" UUID NOT NULL,
    "code_id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "note" TEXT NOT NULL,
    "created_at" TIMESTAMP(0) WITH
        TIME zone NOT NULL,
        "updated_at" TIMESTAMP(0)
    WITH
        TIME zone NOT NULL
);
ALTER TABLE
    "company_categories" ADD PRIMARY KEY("id");
CREATE TABLE "branches"(
    "id" UUID NOT NULL,
    "code_id" TEXT NOT NULL,
    "company_id" UUID NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT NULL,
    "province_id" UUID NULL,
    "district_id" UUID NULL,
    "subdistrict_id" UUID NULL,
    "ward_id" UUID NULL,
    "address" TEXT NULL,
    "pic_name" TEXT NULL,
    "pic_contact" TEXT NULL,
    "note" TEXT NULL,
    "created_at" TIMESTAMP(0) WITH
        TIME zone NULL,
        "updated_at" TIMESTAMP(0)
    WITH
        TIME zone NULL
);
ALTER TABLE
    "branches" ADD PRIMARY KEY("id");
CREATE TABLE "warehouses"(
    "id" BIGINT NOT NULL,
    "code_id" TEXT NOT NULL,
    "branch_id" UUID NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "province_id" UUID NULL,
    "district_id" UUID NULL,
    "subdistrict_id" UUID NULL,
    "ward_id" UUID NULL,
    "address" TEXT NULL,
    "pic_name" TEXT NULL,
    "pic_contact" TEXT NULL,
    "note" TEXT NULL,
    "created_at" TIMESTAMP(0) WITH
        TIME zone NULL,
        "updated_at" TIMESTAMP(0)
    WITH
        TIME zone NULL
);
ALTER TABLE
    "warehouses" ADD PRIMARY KEY("id");
CREATE TABLE "products"(
    "id" BIGINT NOT NULL,
    "code_id" TEXT NOT NULL,
    "warehouse_id" UUID NOT NULL,
    "branch_id" UUID NOT NULL,
    "name" TEXT NOT NULL,
    "category_id" UUID NOT NULL,
    "description" TEXT NOT NULL,
    "note" TEXT NULL,
    "created_at" TIMESTAMP(0) WITH
        TIME zone NULL,
        "updated_at" TIMESTAMP(0)
    WITH
        TIME zone NULL
);
ALTER TABLE
    "products" ADD PRIMARY KEY("id");
CREATE TABLE "partner_categories"(
    "id" UUID NOT NULL,
    "code_id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "note" TEXT NOT NULL,
    "created_at" TIMESTAMP(0) WITH
        TIME zone NOT NULL,
        "updated_at" TIMESTAMP(0)
    WITH
        TIME zone NOT NULL
);
ALTER TABLE
    "partner_categories" ADD PRIMARY KEY("id");
CREATE TABLE "partners"(
    "id" UUID NOT NULL,
    "code_id" TEXT NOT NULL,
    "branch_id" UUID NOT NULL,
    "warehouse_id" BIGINT NOT NULL,
    "name" TEXT NOT NULL,
    "category_id" UUID NOT NULL,
    "description" TEXT NOT NULL,
    "province_id" UUID NULL,
    "district_id" UUID NULL,
    "subdistrict_id" UUID NULL,
    "ward_id" UUID NULL,
    "address" TEXT NULL,
    "pic_name" TEXT NULL,
    "pic_contact" TEXT NULL,
    "note" TEXT NULL,
    "created_at" TIMESTAMP(0) WITH
        TIME zone NULL,
        "updated_at" TIMESTAMP(0)
    WITH
        TIME zone NULL
);
ALTER TABLE
    "partners" ADD PRIMARY KEY("id");
CREATE TABLE "master_provinces"(
    "id" UUID NOT NULL,
    "name" TEXT NOT NULL
);
ALTER TABLE
    "master_provinces" ADD PRIMARY KEY("id");
CREATE TABLE "master_districts"(
    "id" UUID NOT NULL,
    "name" TEXT NOT NULL,
    "province_id" UUID NOT NULL
);
ALTER TABLE
    "master_districts" ADD PRIMARY KEY("id");
CREATE TABLE "master_subdistricts"(
    "id" UUID NOT NULL,
    "name" TEXT NOT NULL,
    "district_id" UUID NOT NULL
);
ALTER TABLE
    "master_subdistricts" ADD PRIMARY KEY("id");
CREATE TABLE "master_wards"(
    "id" UUID NOT NULL,
    "name" TEXT NOT NULL,
    "subdistrict_id" UUID NOT NULL
);
ALTER TABLE
    "master_wards" ADD PRIMARY KEY("id");
CREATE TABLE "master_zipcodes"(
    "id" UUID NOT NULL,
    "code" INTEGER NOT NULL,
    "ward_id" UUID NOT NULL
);
ALTER TABLE
    "master_zipcodes" ADD PRIMARY KEY("id");
CREATE TABLE "product_categories"(
    "id" UUID NOT NULL,
    "code_id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "note" TEXT NOT NULL,
    "created_at" TIMESTAMP(0) WITH
        TIME zone NOT NULL,
        "updated_at" TIMESTAMP(0)
    WITH
        TIME zone NOT NULL
);
ALTER TABLE
    "product_categories" ADD PRIMARY KEY("id");
CREATE TABLE "users"(
    "id" UUID NOT NULL,
    "code_id" TEXT NOT NULL,
    "full_name" TEXT NOT NULL,
    "username" TEXT NOT NULL,
    "enc_password" TEXT NOT NULL,
    "last_login_at" TIMESTAMP(0) WITH
        TIME zone NULL,
        "created_at" TIMESTAMP(0)
    WITH
        TIME zone NULL,
        "updated_at" TIMESTAMP(0)
    WITH
        TIME zone NULL
);
ALTER TABLE
    "users" ADD PRIMARY KEY("id");
ALTER TABLE
    "master_subdistricts" ADD CONSTRAINT "master_subdistricts_district_id_foreign" FOREIGN KEY("district_id") REFERENCES "master_districts"("id");
ALTER TABLE
    "partners" ADD CONSTRAINT "partners_branch_id_foreign" FOREIGN KEY("branch_id") REFERENCES "branches"("id");
ALTER TABLE
    "partners" ADD CONSTRAINT "partners_subdistrict_id_foreign" FOREIGN KEY("subdistrict_id") REFERENCES "master_subdistricts"("id");
ALTER TABLE
    "products" ADD CONSTRAINT "products_category_id_foreign" FOREIGN KEY("category_id") REFERENCES "product_categories"("id");
ALTER TABLE
    "branches" ADD CONSTRAINT "branches_ward_id_foreign" FOREIGN KEY("ward_id") REFERENCES "master_wards"("id");
ALTER TABLE
    "warehouses" ADD CONSTRAINT "warehouses_ward_id_foreign" FOREIGN KEY("ward_id") REFERENCES "master_wards"("id");
ALTER TABLE
    "companies" ADD CONSTRAINT "companies_subdistrict_id_foreign" FOREIGN KEY("subdistrict_id") REFERENCES "master_subdistricts"("id");
ALTER TABLE
    "branches" ADD CONSTRAINT "branches_company_id_foreign" FOREIGN KEY("company_id") REFERENCES "companies"("id");
ALTER TABLE
    "master_districts" ADD CONSTRAINT "master_districts_province_id_foreign" FOREIGN KEY("province_id") REFERENCES "master_provinces"("id");
ALTER TABLE
    "warehouses" ADD CONSTRAINT "warehouses_province_id_foreign" FOREIGN KEY("province_id") REFERENCES "master_provinces"("id");
ALTER TABLE
    "master_zipcodes" ADD CONSTRAINT "master_zipcodes_ward_id_foreign" FOREIGN KEY("ward_id") REFERENCES "master_wards"("id");
ALTER TABLE
    "companies" ADD CONSTRAINT "companies_province_id_foreign" FOREIGN KEY("province_id") REFERENCES "master_provinces"("id");
ALTER TABLE
    "partners" ADD CONSTRAINT "partners_district_id_foreign" FOREIGN KEY("district_id") REFERENCES "master_districts"("id");
ALTER TABLE
    "partners" ADD CONSTRAINT "partners_category_id_foreign" FOREIGN KEY("category_id") REFERENCES "partner_categories"("id");
ALTER TABLE
    "warehouses" ADD CONSTRAINT "warehouses_branch_id_foreign" FOREIGN KEY("branch_id") REFERENCES "branches"("id");
ALTER TABLE
    "products" ADD CONSTRAINT "products_warehouse_id_foreign" FOREIGN KEY("warehouse_id") REFERENCES "warehouses"("id");
ALTER TABLE
    "products" ADD CONSTRAINT "products_branch_id_foreign" FOREIGN KEY("branch_id") REFERENCES "branches"("id");
ALTER TABLE
    "warehouses" ADD CONSTRAINT "warehouses_subdistrict_id_foreign" FOREIGN KEY("subdistrict_id") REFERENCES "master_subdistricts"("id");
ALTER TABLE
    "branches" ADD CONSTRAINT "branches_district_id_foreign" FOREIGN KEY("district_id") REFERENCES "master_districts"("id");
ALTER TABLE
    "branches" ADD CONSTRAINT "branches_province_id_foreign" FOREIGN KEY("province_id") REFERENCES "master_provinces"("id");
ALTER TABLE
    "companies" ADD CONSTRAINT "companies_district_id_foreign" FOREIGN KEY("district_id") REFERENCES "master_districts"("id");
ALTER TABLE
    "partners" ADD CONSTRAINT "partners_province_id_foreign" FOREIGN KEY("province_id") REFERENCES "master_provinces"("id");
ALTER TABLE
    "companies" ADD CONSTRAINT "companies_ward_id_foreign" FOREIGN KEY("ward_id") REFERENCES "master_wards"("id");
ALTER TABLE
    "partners" ADD CONSTRAINT "partners_ward_id_foreign" FOREIGN KEY("ward_id") REFERENCES "master_wards"("id");
ALTER TABLE
    "companies" ADD CONSTRAINT "companies_category_id_foreign" FOREIGN KEY("category_id") REFERENCES "company_categories"("id");
ALTER TABLE
    "partners" ADD CONSTRAINT "partners_warehouse_id_foreign" FOREIGN KEY("warehouse_id") REFERENCES "warehouses"("id");
ALTER TABLE
    "branches" ADD CONSTRAINT "branches_subdistrict_id_foreign" FOREIGN KEY("subdistrict_id") REFERENCES "master_subdistricts"("id");
ALTER TABLE
    "warehouses" ADD CONSTRAINT "warehouses_district_id_foreign" FOREIGN KEY("district_id") REFERENCES "master_districts"("id");
ALTER TABLE
    "master_wards" ADD CONSTRAINT "master_wards_subdistrict_id_foreign" FOREIGN KEY("subdistrict_id") REFERENCES "master_subdistricts"("id");