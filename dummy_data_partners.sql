-- Dummy Data for Partners
-- This file contains sample data for partner categories and partners

-- =============================================
-- PARTNER CATEGORIES
-- =============================================

INSERT INTO partner_categories (id, code_id, name, note, created_at, updated_at) VALUES
('g1111111-1111-1111-1111-111111111111', 'PCAT-SUPPLIER', 'Suppliers', 'Raw material and product suppliers', NOW(), NOW()),
('g1111111-2222-2222-2222-222222222222', 'PCAT-CUSTOMER', 'Customers', 'Business customers and retailers', NOW(), NOW()),
('g1111111-3333-3333-3333-333333333333', 'PCAT-DISTRIBUTOR', 'Distributors', 'Distribution partners and agents', NOW(), NOW()),
('g1111111-4444-4444-4444-444444444444', 'PCAT-VENDOR', 'Vendors', 'Service vendors and contractors', NOW(), NOW());

-- =============================================
-- PARTNERS
-- =============================================

-- Printing Business Partners
INSERT INTO partners (id, code_id, branch_id, warehouse_id, name, category_id, description, province_id, district_id, subdistrict_id, ward_id, address, pic_name, pic_contact, note, created_at, updated_at) VALUES
-- Suppliers
('h1111111-0001-0001-0001-000000000001', 'PART-001', 'c1111111-1111-1111-1111-111111111111', 'd1111111-1111-1111-1111-111111111111', 'Global Paper Industries', 'g1111111-1111-1111-1111-111111111111', 'International paper supplier providing high-quality printing paper and cardstock', '09d2c834-889f-49a8-8713-1858afda4936', 'fb6323dc-54ef-4b14-bb96-551980bdef24', '08c17844-4f84-4439-8b94-541a63cfa66a', '75fca822-285e-4a52-9e18-71566ad9b110', 'Jl. Pabrik Kertas No. 88', 'Michael Chen', '+62-821-1111-2222', 'Net 30 payment terms', NOW(), NOW()),
('h1111111-0001-0001-0001-000000000002', 'PART-002', 'c1111111-1111-1111-1111-111111111111', 'd1111111-1111-1111-1111-111111111111', 'Ink Master Supply Co', 'g1111111-1111-1111-1111-111111111111', 'Premium printing ink and toner supplier for commercial printing', 'e13c585e-31cf-4807-9352-8948d2ba2e94', 'bb15ba9d-6f1b-4ac4-b658-6a2fb799a700', '4b326dec-53ef-41e4-8a03-7695606ee7ed', '71526a3b-be6f-4a51-9b7d-d479cc9d99f1', 'Jl. Kimia Industri No. 45', 'Sarah Williams', '+62-822-3333-4444', 'Bulk discounts available', NOW(), NOW()),

-- Customers
('h1111111-0002-0001-0001-000000000003', 'PART-003', 'c1111111-1111-1111-1111-111111111111', 'd1111111-1111-1111-1111-111111111111', 'Megastore Retail Chain', 'g1111111-2222-2222-2222-222222222222', 'Large retail chain requiring packaging and promotional materials', '09d2c834-889f-49a8-8713-1858afda4936', '2cc428e7-114c-413c-ae49-79206f00bd25', '44b1519b-835e-4221-afa8-81ad2424de19', '1d105465-0de5-49d6-b779-8931ebbb73e5', 'Jl. Retail Plaza No. 100', 'Diana Kusuma', '+62-813-5555-6666', 'Monthly orders', NOW(), NOW()),
('h1111111-0002-0001-0001-000000000004', 'PART-004', 'c2222222-1111-1111-1111-111111111111', 'd1111111-1111-1111-1111-111111111111', 'Corporate Solutions Ltd', 'g1111111-2222-2222-2222-222222222222', 'B2B customer for business cards, letterheads, and corporate branding', '715e36a7-a1db-4220-9302-036964105feb', '99fdeaee-9e72-47e0-a2cc-d6a381932505', 'fe480cd7-2a2e-4b80-ade7-dc6dc326b4ad', '92209704-feb0-4e5b-bd8e-d81d97b9205c', 'Jl. Bisnis Center No. 77', 'Robert Tanoto', '+62-814-7777-8888', 'VIP customer', NOW(), NOW()),

-- Distributors
('h1111111-0003-0001-0001-000000000005', 'PART-005', 'c1111111-1111-2222-2222-222222222222', 'd1111111-1111-2222-2222-222222222222', 'Eastern Distribution Network', 'g1111111-3333-3333-3333-333333333333', 'Regional distributor covering eastern territories', '09d2c834-889f-49a8-8713-1858afda4936', '2cc428e7-114c-413c-ae49-79206f00bd25', '44b1519b-835e-4221-afa8-81ad2424de19', '1d105465-0de5-49d6-b779-8931ebbb73e5', 'Jl. Distribusi Timur No. 66', 'Andi Pratama', '+62-815-9999-1111', 'Commission based', NOW(), NOW()),

-- Hardware Business Partners
-- Suppliers
('h2222222-0001-0001-0001-000000000006', 'PART-006', 'c3333333-1111-1111-1111-111111111111', 'd2222222-1111-1111-1111-111111111111', 'Steel Works Manufacturing', 'g1111111-1111-1111-1111-111111111111', 'Steel and metal products manufacturer and supplier', 'b2f0075b-74d2-4378-8704-2ed9511e153c', 'de69d363-26b5-4201-9360-57b772aba488', 'a7ec6f87-4078-423b-a648-65524d9c38ec', '44e0b8c9-05a1-438e-8018-18f52628814b', 'Jl. Pabrik Baja No. 200', 'Bambang Steel', '+62-816-2222-3333', 'Factory direct pricing', NOW(), NOW()),
('h2222222-0001-0001-0001-000000000007', 'PART-007', 'c3333333-1111-1111-1111-111111111111', 'd2222222-1111-1111-1111-111111111111', 'PowerTool International', 'g1111111-1111-1111-1111-111111111111', 'Authorized distributor of major power tool brands', 'd8e15fd4-4887-4d7c-b3f7-439df754ec6e', 'ebaf7360-3d78-4fe7-8358-c06df13547ea', '57858397-3686-4130-bb78-821b0e0f26ee', '072a6690-9dcb-45df-b795-3a4cca858258', 'Jl. Alat Listrik No. 150', 'James Anderson', '+62-817-4444-5555', 'Warranty support included', NOW(), NOW()),

-- Customers
('h2222222-0002-0001-0001-000000000008', 'PART-008', 'c3333333-1111-1111-1111-111111111111', 'd2222222-1111-1111-1111-111111111111', 'City Construction Group', 'g1111111-2222-2222-2222-222222222222', 'Major construction company, regular bulk orders', 'b2f0075b-74d2-4378-8704-2ed9511e153c', 'de69d363-26b5-4201-9360-57b772aba488', 'a7ec6f87-4078-423b-a648-65524d9c38ec', '44e0b8c9-05a1-438e-8018-18f52628814b', 'Jl. Konstruksi No. 300', 'Ir. Susanto', '+62-818-6666-7777', 'Credit approved', NOW(), NOW()),
('h2222222-0002-0001-0001-000000000009', 'PART-009', 'c3333333-1111-2222-2222-222222222222', 'd2222222-1111-2222-2222-222222222222', 'Home Renovation Specialist', 'g1111111-2222-2222-2222-222222222222', 'Home renovation contractor, weekly purchases', 'b2f0075b-74d2-4378-8704-2ed9511e153c', '37c2703e-6754-4a8e-a64e-e2f5fd49e4ed', '631ae4f2-ebf8-4683-96f2-48f042ad8fbf', '257dcc25-811a-4596-b0e0-5990affec52d', 'Jl. Renovasi No. 55', 'Tono Hartono', '+62-819-8888-9999', 'Repeat customer', NOW(), NOW()),

-- Vendors
('h2222222-0004-0001-0001-000000000010', 'PART-010', 'c3333333-1111-1111-1111-111111111111', 'd2222222-1111-1111-1111-111111111111', 'Express Logistics Services', 'g1111111-4444-4444-4444-444444444444', 'Logistics and delivery service provider', '224fabdb-a0df-473f-b41d-6b8f8686c3e7', 'e8d1dd17-7456-429b-ac29-13405c66ebf5', '3d61964a-6fee-4d05-895c-ee89466aac88', 'ec304291-1ce5-49fc-b3a1-36e5b3c93036', 'Jl. Logistik Hub No. 400', 'Agung Delivery', '+62-820-1111-2222', 'Same day delivery available', NOW(), NOW());
