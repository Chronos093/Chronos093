USE carros;

INSERT INTO lojas (nome, telefone, email, endereco, num_endereco, bairro, cep, cidade, estado) VALUES
('Loja Centro', '1198765432', 'contato@lojacentro.com', 'Rua Principal', '123', 'Centro', '01000-000', 'São Paulo', 'São Paulo'),
('Loja Sul', '1197654321', 'contato@lojasul.com', 'Avenida Sul', '456', 'Sul', '02000-000', 'São Paulo', 'São Paulo'),
('Loja Norte', '1196543210', 'contato@lojanorte.com', 'Rua Norte', '789', 'Norte', '03000-000', 'Campinas', 'São Paulo');

INSERT INTO marcas (nome_marcar, origem) VALUES
('Toyota', 'Japão'),
('Honda', 'Japão'),
('Chevrolet', 'Estados Unidos'),
('Ford', 'Estados Unidos'),
('Volkswagen', 'Alemanha');

INSERT INTO inventario (modelo, transmissao, motor, combustivel, marcas_id, loja_id) VALUES
('Corolla', 'Automático', '1.8', 'Gasolina', 1, 1),
('Civic', 'Manual', '2.0', 'Flex', 2, 2),
('Onix', 'Automático', '1.4', 'Flex', 3, 1),
('Focus', 'Manual', '2.0', 'Gasolina', 4, 3),
('Gol', 'Automático', '1.0', 'Flex', 5, 2);

INSERT INTO clientes (nome, sobrenome, telefone, endereco, num_endereco, bairro, cep, cidade, estado, email) VALUES
('Carlos', 'Silva', '1199123456', 'Rua A', '123', 'Centro', '12345-678', 'São Paulo', 'São Paulo', 'carlos.silva@email.com'),
('Ana', 'Oliveira', '1199987654', 'Rua B', '456', 'Sul', '23456-789', 'Santos', 'São Paulo', 'ana.oliveira@email.com'),
('João', 'Santos', '1199876543', 'Rua C', '789', 'Leste', '34567-890', 'Campinas', 'São Paulo', 'joao.santos@email.com');

INSERT INTO vendedor (nome, sobrenome, loja_id, telefone, endereco, num_endereco, bairro, cep, cidade, estado, email) VALUES
('Lucas', 'Almeida', 1, '1198765432', 'Rua Vendas', '101', 'Centro', '12345-678', 'São Paulo', 'São Paulo', 'lucas.almeida@email.com'),
('Marina', 'Costa', 2, '1196543210', 'Avenida Comercial', '202', 'Sul', '23456-789', 'Santos', 'São Paulo', 'marina.costa@email.com'),
('Pedro', 'Souza', 3, '1194321098', 'Rua Central', '303', 'Norte', '34567-890', 'Campinas', 'São Paulo', 'pedro.souza@email.com');

INSERT INTO aluguel (clientes_id, vendedor_id, iventario_id, lojas_id) VALUES
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 1),
(1, 3, 4, 3),
(2, 1, 5, 2);
