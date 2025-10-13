-- Dummy Data for Printing and Hardware Business
-- This file contains sample data for companies, branches, warehouses, and products

-- =============================================
-- COMPANY CATEGORIES
-- =============================================

INSERT INTO company_categories (id, code_id, name, note, created_at, updated_at) VALUES
('a1b2c3d4-1111-1111-1111-111111111111', 'CC-PRINT', 'Printing & Publishing', 'Companies in printing, publishing, and related services', NOW(), NOW()),
('a1b2c3d4-2222-2222-2222-222222222222', 'CC-HARDWARE', 'Hardware & Tools', 'Companies dealing with hardware, tools, and equipment', NOW(), NOW());

-- =============================================
-- COMPANIES
-- =============================================

-- Printing Companies
INSERT INTO companies (id, code_id, name, category_id, description, province_id, district_id, subdistrict_id, ward_id, zipcode_id, address, pic_name, pic_contact, note, created_at, updated_at) VALUES
('b1111111-1111-1111-1111-111111111111', 'COMP-001', 'PrintMaster Solutions', 'a1b2c3d4-1111-1111-1111-111111111111', 'Leading provider of commercial printing services including offset, digital, and large format printing', '09d2c834-889f-49a8-8713-1858afda4936', 'fb6323dc-54ef-4b14-bb96-551980bdef24', '08c17844-4f84-4439-8b94-541a63cfa66a', '75fca822-285e-4a52-9e18-71566ad9b110', '9d426d15-38f3-40e3-9a61-4cff0317e05c', 'Jl. Industri No. 45, Kawasan Industri', 'Ahmad Fauzi', '+62-812-3456-7890', 'Established in 2010, ISO certified', NOW(), NOW()),
('b1111111-2222-2222-2222-222222222222', 'COMP-002', 'Creative Print Hub', 'a1b2c3d4-1111-1111-1111-111111111111', 'Specializing in custom packaging, branding materials, and promotional printing', 'e13c585e-31cf-4807-9352-8948d2ba2e94', 'bb15ba9d-6f1b-4ac4-b658-6a2fb799a700', '4b326dec-53ef-41e4-8a03-7695606ee7ed', '71526a3b-be6f-4a51-9b7d-d479cc9d99f1', 'f57558b7-b5dc-4ea7-a7f1-e757ac07d79d', 'Jl. Raya Printing No. 12', 'Siti Nurhaliza', '+62-813-9876-5432', 'Award-winning design team', NOW(), NOW()),
('b1111111-3333-3333-3333-333333333333', 'COMP-003', 'Digital Print Express', 'a1b2c3d4-1111-1111-1111-111111111111', '24/7 digital printing services with same-day delivery options', '715e36a7-a1db-4220-9302-036964105feb', '99fdeaee-9e72-47e0-a2cc-d6a381932505', 'fe480cd7-2a2e-4b80-ade7-dc6dc326b4ad', '92209704-feb0-4e5b-bd8e-d81d97b9205c', '5ce137b2-4b20-42df-8550-88b3a0d4bdc2', 'Jl. Percetakan Raya No. 78', 'Budi Santoso', '+62-821-5555-1234', 'Fast turnaround time', NOW(), NOW());

-- Hardware Companies  
INSERT INTO companies (id, code_id, name, category_id, description, province_id, district_id, subdistrict_id, ward_id, zipcode_id, address, pic_name, pic_contact, note, created_at, updated_at) VALUES
('b2222222-1111-1111-1111-111111111111', 'COMP-004', 'Mega Hardware Supply', 'a1b2c3d4-2222-2222-2222-222222222222', 'Comprehensive hardware store offering construction materials, tools, and home improvement products', 'b2f0075b-74d2-4378-8704-2ed9511e153c', 'de69d363-26b5-4201-9360-57b772aba488', 'a7ec6f87-4078-423b-a648-65524d9c38ec', '44e0b8c9-05a1-438e-8018-18f52628814b', '93e6a7c9-81ce-4a18-96e4-c6c0d7e17b22', 'Jl. Hardware Center No. 101', 'Eko Prasetyo', '+62-815-7777-8888', 'Wholesale and retail available', NOW(), NOW()),
('b2222222-2222-2222-2222-222222222222', 'COMP-005', 'Pro Tools Indonesia', 'a1b2c3d4-2222-2222-2222-222222222222', 'Professional grade tools and equipment for construction and manufacturing industries', 'd8e15fd4-4887-4d7c-b3f7-439df754ec6e', 'ebaf7360-3d78-4fe7-8358-c06df13547ea', '57858397-3686-4130-bb78-821b0e0f26ee', '072a6690-9dcb-45df-b795-3a4cca858258', '0353c411-c00b-4b93-87ff-a2c9c7825500', 'Jl. Industri Alat No. 88', 'Dewi Lestari', '+62-822-4444-3333', 'Authorized dealer of major brands', NOW(), NOW()),
('b2222222-3333-3333-3333-333333333333', 'COMP-006', 'BuildMart Hardware', 'a1b2c3d4-2222-2222-2222-222222222222', 'One-stop shop for construction and building materials with expert consultation', '224fabdb-a0df-473f-b41d-6b8f8686c3e7', 'e8d1dd17-7456-429b-ac29-13405c66ebf5', '3d61964a-6fee-4d05-895c-ee89466aac88', 'ec304291-1ce5-49fc-b3a1-36e5b3c93036', '374b052b-34bd-4041-a26d-990f6ad75f3f', 'Jl. Bangunan Utama No. 55', 'Rizky Firmansyah', '+62-811-2222-9999', 'Free delivery for bulk orders', NOW(), NOW());

-- =============================================
-- BRANCHES
-- =============================================

-- PrintMaster Solutions Branches
INSERT INTO branches (id, code_id, company_id, name, description, province_id, district_id, subdistrict_id, ward_id, address, pic_name, pic_contact, note, created_at, updated_at) VALUES
('c1111111-1111-1111-1111-111111111111', 'BR-001-01', 'b1111111-1111-1111-1111-111111111111', 'PrintMaster HQ', 'Head office and main production facility', '09d2c834-889f-49a8-8713-1858afda4936', 'fb6323dc-54ef-4b14-bb96-551980bdef24', '08c17844-4f84-4439-8b94-541a63cfa66a', '75fca822-285e-4a52-9e18-71566ad9b110', 'Jl. Industri No. 45', 'Ahmad Fauzi', '+62-812-3456-7890', 'Main branch', NOW(), NOW()),
('c1111111-1111-2222-2222-222222222222', 'BR-001-02', 'b1111111-1111-1111-1111-111111111111', 'PrintMaster East Branch', 'Eastern regional office', '09d2c834-889f-49a8-8713-1858afda4936', '2cc428e7-114c-413c-ae49-79206f00bd25', '44b1519b-835e-4221-afa8-81ad2424de19', '1d105465-0de5-49d6-b779-8931ebbb73e5', 'Jl. Timur Raya No. 23', 'Hendra Wijaya', '+62-813-1111-2222', 'Branch office', NOW(), NOW());

-- Creative Print Hub Branches
INSERT INTO branches (id, code_id, company_id, name, description, province_id, district_id, subdistrict_id, ward_id, address, pic_name, pic_contact, note, created_at, updated_at) VALUES
('c2222222-1111-1111-1111-111111111111', 'BR-002-01', 'b1111111-2222-2222-2222-222222222222', 'Creative Print Main', 'Main facility', 'e13c585e-31cf-4807-9352-8948d2ba2e94', 'bb15ba9d-6f1b-4ac4-b658-6a2fb799a700', '4b326dec-53ef-41e4-8a03-7695606ee7ed', '71526a3b-be6f-4a51-9b7d-d479cc9d99f1', 'Jl. Raya Printing No. 12', 'Siti Nurhaliza', '+62-813-9876-5432', 'Main branch', NOW(), NOW());

-- Mega Hardware Supply Branches
INSERT INTO branches (id, code_id, company_id, name, description, province_id, district_id, subdistrict_id, ward_id, address, pic_name, pic_contact, note, created_at, updated_at) VALUES
('c3333333-1111-1111-1111-111111111111', 'BR-004-01', 'b2222222-1111-1111-1111-111111111111', 'Mega Hardware Central', 'Central warehouse and showroom', 'b2f0075b-74d2-4378-8704-2ed9511e153c', 'de69d363-26b5-4201-9360-57b772aba488', 'a7ec6f87-4078-423b-a648-65524d9c38ec', '44e0b8c9-05a1-438e-8018-18f52628814b', 'Jl. Hardware Center No. 101', 'Eko Prasetyo', '+62-815-7777-8888', 'Main branch', NOW(), NOW()),
('c3333333-1111-2222-2222-222222222222', 'BR-004-02', 'b2222222-1111-1111-1111-111111111111', 'Mega Hardware South', 'Southern branch', 'b2f0075b-74d2-4378-8704-2ed9511e153c', '37c2703e-6754-4a8e-a64e-e2f5fd49e4ed', '631ae4f2-ebf8-4683-96f2-48f042ad8fbf', '257dcc25-811a-4596-b0e0-5990affec52d', 'Jl. Selatan No. 44', 'Linda Rahayu', '+62-816-5555-6666', 'Branch office', NOW(), NOW());

-- Pro Tools Indonesia Branches
INSERT INTO branches (id, code_id, company_id, name, description, province_id, district_id, subdistrict_id, ward_id, address, pic_name, pic_contact, note, created_at, updated_at) VALUES
('c4444444-1111-1111-1111-111111111111', 'BR-005-01', 'b2222222-2222-2222-2222-222222222222', 'Pro Tools Main Office', 'Main sales and service center', 'd8e15fd4-4887-4d7c-b3f7-439df754ec6e', 'ebaf7360-3d78-4fe7-8358-c06df13547ea', '57858397-3686-4130-bb78-821b0e0f26ee', '072a6690-9dcb-45df-b795-3a4cca858258', 'Jl. Industri Alat No. 88', 'Dewi Lestari', '+62-822-4444-3333', 'Main branch', NOW(), NOW());

-- =============================================
-- WAREHOUSES
-- =============================================

-- PrintMaster Warehouses
INSERT INTO warehouses (id, code_id, branch_id, name, description, province_id, district_id, subdistrict_id, ward_id, address, pic_name, pic_contact, note, created_at, updated_at) VALUES
('d1111111-1111-1111-1111-111111111111', 'WH-001-01', 'c1111111-1111-1111-1111-111111111111', 'PrintMaster Main Warehouse', 'Main paper and materials storage', '09d2c834-889f-49a8-8713-1858afda4936', 'fb6323dc-54ef-4b14-bb96-551980bdef24', '08c17844-4f84-4439-8b94-541a63cfa66a', '75fca822-285e-4a52-9e18-71566ad9b110', 'Jl. Gudang No. 10', 'Agus Santoso', '+62-817-1234-5678', 'Climate controlled', NOW(), NOW()),
('d1111111-1111-2222-2222-222222222222', 'WH-001-02', 'c1111111-1111-2222-2222-222222222222', 'PrintMaster East Warehouse', 'Regional distribution center', '09d2c834-889f-49a8-8713-1858afda4936', '2cc428e7-114c-413c-ae49-79206f00bd25', '44b1519b-835e-4221-afa8-81ad2424de19', '1d105465-0de5-49d6-b779-8931ebbb73e5', 'Jl. Timur Gudang No. 5', 'Yudi Prabowo', '+62-818-2222-3333', 'Regional warehouse', NOW(), NOW());

-- Mega Hardware Warehouses
INSERT INTO warehouses (id, code_id, branch_id, name, description, province_id, district_id, subdistrict_id, ward_id, address, pic_name, pic_contact, note, created_at, updated_at) VALUES
('d2222222-1111-1111-1111-111111111111', 'WH-004-01', 'c3333333-1111-1111-1111-111111111111', 'Mega Hardware Main Warehouse', 'Large-scale hardware storage facility', 'b2f0075b-74d2-4378-8704-2ed9511e153c', 'de69d363-26b5-4201-9360-57b772aba488', 'a7ec6f87-4078-423b-a648-65524d9c38ec', '44e0b8c9-05a1-438e-8018-18f52628814b', 'Jl. Gudang Besar No. 20', 'Bambang Suprapto', '+62-819-7777-8888', 'Heavy duty racking', NOW(), NOW()),
('d2222222-1111-2222-2222-222222222222', 'WH-004-02', 'c3333333-1111-2222-2222-222222222222', 'Mega Hardware South Warehouse', 'Southern distribution hub', 'b2f0075b-74d2-4378-8704-2ed9511e153c', '37c2703e-6754-4a8e-a64e-e2f5fd49e4ed', '631ae4f2-ebf8-4683-96f2-48f042ad8fbf', '257dcc25-811a-4596-b0e0-5990affec52d', 'Jl. Gudang Selatan No. 15', 'Fitri Handayani', '+62-820-6666-7777', 'Distribution center', NOW(), NOW());

-- =============================================
-- PRODUCT CATEGORIES
-- =============================================

INSERT INTO product_categories (id, code_id, name, note, created_at, updated_at) VALUES
-- Printing Categories
('e1111111-1111-1111-1111-111111111111', 'PC-PAPER', 'Printing Paper', 'Various types of paper for printing', NOW(), NOW()),
('e1111111-2222-2222-2222-222222222222', 'PC-INK', 'Ink & Toner', 'Printing inks and toner cartridges', NOW(), NOW()),
('e1111111-3333-3333-3333-333333333333', 'PC-MACHINE', 'Printing Machines', 'Offset and digital printing equipment', NOW(), NOW()),
('e1111111-4444-4444-4444-444444444444', 'PC-PACKAGE', 'Packaging Materials', 'Boxes, bags, and packaging supplies', NOW(), NOW()),

-- Hardware Categories
('e2222222-1111-1111-1111-111111111111', 'PC-HANDTOOL', 'Hand Tools', 'Manual tools and equipment', NOW(), NOW()),
('e2222222-2222-2222-2222-222222222222', 'PC-POWERTOOLS', 'Power Tools', 'Electric and pneumatic tools', NOW(), NOW()),
('e2222222-3333-3333-3333-333333333333', 'PC-FASTENER', 'Fasteners', 'Screws, bolts, nuts, and anchors', NOW(), NOW()),
('e2222222-4444-4444-4444-444444444444', 'PC-BUILDING', 'Building Materials', 'Construction and building supplies', NOW(), NOW());

-- =============================================
-- PRODUCTS
-- =============================================

-- Printing Products
INSERT INTO products (id, code_id, warehouse_id, branch_id, name, category_id, description, note, created_at, updated_at) VALUES
-- Paper Products
('f1111111-0001-0001-0001-000000000001', 'PRD-PRINT-001', 'd1111111-1111-1111-1111-111111111111', 'c1111111-1111-1111-1111-111111111111', 'A4 Copy Paper 80gsm', 'e1111111-1111-1111-1111-111111111111', 'High quality white copy paper, 500 sheets per ream, suitable for all copiers and printers', 'Best seller', NOW(), NOW()),
('f1111111-0001-0001-0001-000000000002', 'PRD-PRINT-002', 'd1111111-1111-1111-1111-111111111111', 'c1111111-1111-1111-1111-111111111111', 'A3 Art Paper 120gsm', 'e1111111-1111-1111-1111-111111111111', 'Premium glossy art paper for brochures and posters', 'High gloss finish', NOW(), NOW()),
('f1111111-0001-0001-0001-000000000003', 'PRD-PRINT-003', 'd1111111-1111-1111-1111-111111111111', 'c1111111-1111-1111-1111-111111111111', 'Cardstock Paper 250gsm', 'e1111111-1111-1111-1111-111111111111', 'Heavy cardstock for business cards and invitations', 'Various colors available', NOW(), NOW()),

-- Ink & Toner
('f1111111-0002-0001-0001-000000000004', 'PRD-PRINT-004', 'd1111111-1111-1111-1111-111111111111', 'c1111111-1111-1111-1111-111111111111', 'CMYK Ink Set - Offset', 'e1111111-2222-2222-2222-222222222222', 'Professional grade offset printing ink set, vibrant colors, fast drying', 'Compatible with major brands', NOW(), NOW()),
('f1111111-0002-0001-0001-000000000005', 'PRD-PRINT-005', 'd1111111-1111-1111-1111-111111111111', 'c1111111-1111-1111-1111-111111111111', 'Laser Toner Cartridge - Black', 'e1111111-2222-2222-2222-222222222222', 'High yield laser toner, 5000 pages', 'OEM quality', NOW(), NOW()),

-- Machines
('f1111111-0003-0001-0001-000000000006', 'PRD-PRINT-006', 'd1111111-1111-1111-1111-111111111111', 'c1111111-1111-1111-1111-111111111111', 'Digital Printer - Large Format', 'e1111111-3333-3333-3333-333333333333', 'Industrial large format digital printer, 1.6m width, eco-solvent ink system', 'Warranty 2 years', NOW(), NOW()),
('f1111111-0003-0001-0001-000000000007', 'PRD-PRINT-007', 'd1111111-1111-2222-2222-222222222222', 'c1111111-1111-2222-2222-222222222222', 'Offset Printing Machine 4-Color', 'e1111111-3333-3333-3333-333333333333', 'High-speed 4-color offset press, automatic feeder', 'Refurbished available', NOW(), NOW()),

-- Packaging
('f1111111-0004-0001-0001-000000000008', 'PRD-PRINT-008', 'd1111111-1111-1111-1111-111111111111', 'c1111111-1111-1111-1111-111111111111', 'Corrugated Box - Medium', 'e1111111-4444-4444-4444-444444444444', 'Brown corrugated shipping box, 40x30x25cm, single wall', 'Bulk pricing available', NOW(), NOW()),
('f1111111-0004-0001-0001-000000000009', 'PRD-PRINT-009', 'd1111111-1111-1111-1111-111111111111', 'c1111111-1111-1111-1111-111111111111', 'Custom Paper Bag with Handle', 'e1111111-4444-4444-4444-444444444444', 'Eco-friendly kraft paper bag with twisted handle, customizable print', 'Minimum order 1000 pcs', NOW(), NOW());

-- Hardware Products
-- Hand Tools
INSERT INTO products (id, code_id, warehouse_id, branch_id, name, category_id, description, note, created_at, updated_at) VALUES
('f2222222-0001-0001-0001-000000000001', 'PRD-HARD-001', 'd2222222-1111-1111-1111-111111111111', 'c3333333-1111-1111-1111-111111111111', 'Hammer - Claw 16oz', 'e2222222-1111-1111-1111-111111111111', 'Steel claw hammer with fiberglass handle, shock-absorbing grip', 'Lifetime warranty', NOW(), NOW()),
('f2222222-0001-0001-0001-000000000002', 'PRD-HARD-002', 'd2222222-1111-1111-1111-111111111111', 'c3333333-1111-1111-1111-111111111111', 'Screwdriver Set 6pcs', 'e2222222-1111-1111-1111-111111111111', 'Professional screwdriver set with magnetic tips, CR-V steel', 'Popular item', NOW(), NOW()),
('f2222222-0001-0001-0001-000000000003', 'PRD-HARD-003', 'd2222222-1111-1111-1111-111111111111', 'c3333333-1111-1111-1111-111111111111', 'Adjustable Wrench 12"', 'e2222222-1111-1111-1111-111111111111', 'Heavy duty adjustable wrench, chrome vanadium steel', 'Industrial grade', NOW(), NOW()),
('f2222222-0001-0001-0001-000000000004', 'PRD-HARD-004', 'd2222222-1111-2222-2222-222222222222', 'c3333333-1111-2222-2222-222222222222', 'Pliers Set 3pcs', 'e2222222-1111-1111-1111-111111111111', 'Combination, long nose, and cutting pliers with cushion grip', 'Value pack', NOW(), NOW()),

-- Power Tools
('f2222222-0002-0001-0001-000000000005', 'PRD-HARD-005', 'd2222222-1111-1111-1111-111111111111', 'c3333333-1111-1111-1111-111111111111', 'Electric Drill 13mm - Corded', 'e2222222-2222-2222-2222-222222222222', '710W corded electric drill with keyless chuck, variable speed control', 'Includes drill bits', NOW(), NOW()),
('f2222222-0002-0001-0001-000000000006', 'PRD-HARD-006', 'd2222222-1111-1111-1111-111111111111', 'c3333333-1111-1111-1111-111111111111', 'Angle Grinder 4"', 'e2222222-2222-2222-2222-222222222222', '850W angle grinder with safety guard and side handle', 'Heavy duty', NOW(), NOW()),
('f2222222-0002-0001-0001-000000000007', 'PRD-HARD-007', 'd2222222-1111-1111-1111-111111111111', 'c3333333-1111-1111-1111-111111111111', 'Circular Saw 7.25"', 'e2222222-2222-2222-2222-222222222222', '1400W circular saw with laser guide and dust blower', 'Professional grade', NOW(), NOW()),

-- Fasteners
('f2222222-0003-0001-0001-000000000008', 'PRD-HARD-008', 'd2222222-1111-1111-1111-111111111111', 'c3333333-1111-1111-1111-111111111111', 'Wood Screws #8 x 2" (Box of 100)', 'e2222222-3333-3333-3333-333333333333', 'Phillips head wood screws, zinc plated', 'Bulk available', NOW(), NOW()),
('f2222222-0003-0001-0001-000000000009', 'PRD-HARD-009', 'd2222222-1111-1111-1111-111111111111', 'c3333333-1111-1111-1111-111111111111', 'Hex Bolt M10x50 with Nut (Box of 50)', 'e2222222-3333-3333-3333-333333333333', 'Galvanized hex bolt with matching nut and washer', 'Various sizes', NOW(), NOW()),
('f2222222-0003-0001-0001-000000000010', 'PRD-HARD-010', 'd2222222-1111-2222-2222-222222222222', 'c3333333-1111-2222-2222-222222222222', 'Anchor Bolt Set - Heavy Duty', 'e2222222-3333-3333-3333-333333333333', 'Expansion anchor bolts for concrete, assorted sizes', 'For concrete walls', NOW(), NOW()),

-- Building Materials
('f2222222-0004-0001-0001-000000000011', 'PRD-HARD-011', 'd2222222-1111-1111-1111-111111111111', 'c3333333-1111-1111-1111-111111111111', 'Cement - Portland Type I (50kg)', 'e2222222-4444-4444-4444-444444444444', 'Premium Portland cement for general construction', 'Minimum 10 bags', NOW(), NOW()),
('f2222222-0004-0001-0001-000000000012', 'PRD-HARD-012', 'd2222222-1111-1111-1111-111111111111', 'c3333333-1111-1111-1111-111111111111', 'PVC Pipe 4" x 4m', 'e2222222-4444-4444-4444-444444444444', 'Heavy duty PVC pipe for plumbing and drainage', 'SNI certified', NOW(), NOW()),
('f2222222-0004-0001-0001-000000000013', 'PRD-HARD-013', 'd2222222-1111-1111-1111-111111111111', 'c3333333-1111-1111-1111-111111111111', 'Steel Rebar 10mm x 12m', 'e2222222-4444-4444-4444-444444444444', 'High tensile deformed steel bar for concrete reinforcement', 'Cut to size available', NOW(), NOW());
