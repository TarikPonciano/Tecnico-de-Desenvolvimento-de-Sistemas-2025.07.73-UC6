--
-- PostgreSQL database dump
--

-- Dumped from database version 17.6
-- Dumped by pg_dump version 17.5

-- Started on 2025-09-02 13:18:14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 26224)
-- Name: cliente; Type: TABLE; Schema: public; Owner: avnadmin
--

CREATE TABLE public.cliente (
    id_cliente integer NOT NULL,
    nome_cliente character varying(255) NOT NULL
);


ALTER TABLE public.cliente OWNER TO avnadmin;

--
-- TOC entry 217 (class 1259 OID 26223)
-- Name: cliente_id_cliente_seq; Type: SEQUENCE; Schema: public; Owner: avnadmin
--

ALTER TABLE public.cliente ALTER COLUMN id_cliente ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.cliente_id_cliente_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 224 (class 1259 OID 26254)
-- Name: item; Type: TABLE; Schema: public; Owner: avnadmin
--

CREATE TABLE public.item (
    id_item integer NOT NULL,
    venda_id integer NOT NULL,
    produto_id integer NOT NULL,
    quantidade_item integer DEFAULT 1 NOT NULL,
    preco_item numeric(6,2) DEFAULT 0.00 NOT NULL,
    CONSTRAINT chk_preco CHECK ((preco_item >= (0)::numeric)),
    CONSTRAINT chk_qtd CHECK ((quantidade_item >= 1))
);


ALTER TABLE public.item OWNER TO avnadmin;

--
-- TOC entry 223 (class 1259 OID 26253)
-- Name: item_id_item_seq; Type: SEQUENCE; Schema: public; Owner: avnadmin
--

ALTER TABLE public.item ALTER COLUMN id_item ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.item_id_item_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 220 (class 1259 OID 26230)
-- Name: produto; Type: TABLE; Schema: public; Owner: avnadmin
--

CREATE TABLE public.produto (
    id_produto integer NOT NULL,
    nome_produto character varying(255) NOT NULL,
    preco_produto numeric(6,2) DEFAULT 0.00 NOT NULL,
    estoque_produto integer DEFAULT 0 NOT NULL,
    CONSTRAINT chk_estoque CHECK ((estoque_produto >= 0)),
    CONSTRAINT chk_preco CHECK ((preco_produto >= (0)::numeric))
);


ALTER TABLE public.produto OWNER TO avnadmin;

--
-- TOC entry 219 (class 1259 OID 26229)
-- Name: produto_id_produto_seq; Type: SEQUENCE; Schema: public; Owner: avnadmin
--

ALTER TABLE public.produto ALTER COLUMN id_produto ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.produto_id_produto_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 222 (class 1259 OID 26240)
-- Name: venda; Type: TABLE; Schema: public; Owner: avnadmin
--

CREATE TABLE public.venda (
    id_venda integer NOT NULL,
    cliente_id integer NOT NULL,
    total_venda numeric(10,2) DEFAULT 0.00 NOT NULL,
    data_venda timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT chk_total CHECK ((total_venda >= (0)::numeric))
);


ALTER TABLE public.venda OWNER TO avnadmin;

--
-- TOC entry 221 (class 1259 OID 26239)
-- Name: venda_id_venda_seq; Type: SEQUENCE; Schema: public; Owner: avnadmin
--

ALTER TABLE public.venda ALTER COLUMN id_venda ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.venda_id_venda_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4458 (class 0 OID 26224)
-- Dependencies: 218
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: avnadmin
--

COPY public.cliente (id_cliente, nome_cliente) FROM stdin;
1	Jonathan Ferreira
2	Manoel Gomes
\.


--
-- TOC entry 4464 (class 0 OID 26254)
-- Dependencies: 224
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: avnadmin
--

COPY public.item (id_item, venda_id, produto_id, quantidade_item, preco_item) FROM stdin;
1	9	1	10	2.59
\.


--
-- TOC entry 4460 (class 0 OID 26230)
-- Dependencies: 220
-- Data for Name: produto; Type: TABLE DATA; Schema: public; Owner: avnadmin
--

COPY public.produto (id_produto, nome_produto, preco_produto, estoque_produto) FROM stdin;
1	Nescauzinho 180ml	2.59	10
\.


--
-- TOC entry 4462 (class 0 OID 26240)
-- Dependencies: 222
-- Data for Name: venda; Type: TABLE DATA; Schema: public; Owner: avnadmin
--

COPY public.venda (id_venda, cliente_id, total_venda, data_venda) FROM stdin;
1	2	0.00	2025-09-02 13:57:43.043917
2	1	0.00	2025-09-02 13:58:02.708909
3	1	0.00	2025-09-03 11:40:10.48875
4	2	0.00	2025-09-03 12:28:16.724189
5	2	0.00	2025-09-03 12:29:26.363817
6	2	0.00	2025-09-03 12:30:13.78225
7	2	0.00	2025-09-03 12:31:09.403934
9	2	25.90	2025-09-03 12:31:44.863754
\.


--
-- TOC entry 4470 (class 0 OID 0)
-- Dependencies: 217
-- Name: cliente_id_cliente_seq; Type: SEQUENCE SET; Schema: public; Owner: avnadmin
--

SELECT pg_catalog.setval('public.cliente_id_cliente_seq', 3, true);


--
-- TOC entry 4471 (class 0 OID 0)
-- Dependencies: 223
-- Name: item_id_item_seq; Type: SEQUENCE SET; Schema: public; Owner: avnadmin
--

SELECT pg_catalog.setval('public.item_id_item_seq', 1, true);


--
-- TOC entry 4472 (class 0 OID 0)
-- Dependencies: 219
-- Name: produto_id_produto_seq; Type: SEQUENCE SET; Schema: public; Owner: avnadmin
--

SELECT pg_catalog.setval('public.produto_id_produto_seq', 1, true);


--
-- TOC entry 4473 (class 0 OID 0)
-- Dependencies: 221
-- Name: venda_id_venda_seq; Type: SEQUENCE SET; Schema: public; Owner: avnadmin
--

SELECT pg_catalog.setval('public.venda_id_venda_seq', 9, true);


--
-- TOC entry 4302 (class 2606 OID 26228)
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: avnadmin
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (id_cliente);


--
-- TOC entry 4308 (class 2606 OID 26262)
-- Name: item item_pkey; Type: CONSTRAINT; Schema: public; Owner: avnadmin
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT item_pkey PRIMARY KEY (id_item);


--
-- TOC entry 4304 (class 2606 OID 26238)
-- Name: produto produto_pkey; Type: CONSTRAINT; Schema: public; Owner: avnadmin
--

ALTER TABLE ONLY public.produto
    ADD CONSTRAINT produto_pkey PRIMARY KEY (id_produto);


--
-- TOC entry 4306 (class 2606 OID 26247)
-- Name: venda venda_pkey; Type: CONSTRAINT; Schema: public; Owner: avnadmin
--

ALTER TABLE ONLY public.venda
    ADD CONSTRAINT venda_pkey PRIMARY KEY (id_venda);


--
-- TOC entry 4309 (class 2606 OID 26248)
-- Name: venda fk_cliente_venda; Type: FK CONSTRAINT; Schema: public; Owner: avnadmin
--

ALTER TABLE ONLY public.venda
    ADD CONSTRAINT fk_cliente_venda FOREIGN KEY (cliente_id) REFERENCES public.cliente(id_cliente);


--
-- TOC entry 4310 (class 2606 OID 26268)
-- Name: item fk_produto_item; Type: FK CONSTRAINT; Schema: public; Owner: avnadmin
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT fk_produto_item FOREIGN KEY (produto_id) REFERENCES public.produto(id_produto);


--
-- TOC entry 4311 (class 2606 OID 26263)
-- Name: item fk_venda_item; Type: FK CONSTRAINT; Schema: public; Owner: avnadmin
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT fk_venda_item FOREIGN KEY (venda_id) REFERENCES public.venda(id_venda);


-- Completed on 2025-09-02 13:18:32

--
-- PostgreSQL database dump complete
--

