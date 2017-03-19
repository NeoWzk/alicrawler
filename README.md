# alicrawler

This is a fully functional working spider for crawling aliexpress.com categories product. 
1. you will have to set up your own config.py for the sql database
2. To get your own proxy IP too (you know why you have to do so,right?)
3. to behave well for aliexpress.com :D
4. if you encounter any problem, you know how to reach me :DD

to run this spider, it is suggested to create a table as this:

DROP TABLE IF EXISTS `db_aeproductdata`;
CREATE TABLE `db_aeproductdata` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `product_id` varchar(15) DEFAULT NULL,
  `product_title` varchar(300) DEFAULT NULL,
  `product_url` varchar(1000) DEFAULT NULL,
  `product_unit_price` varchar(20) DEFAULT NULL,
  `product_unit` varchar(45) DEFAULT NULL,
  `product_sold_num` int(11) DEFAULT NULL,
  `product_img_url` varchar(300) DEFAULT NULL,
  `product_rateimg_url` varchar(120) DEFAULT NULL,
  `product_feedback_num` int(10) DEFAULT NULL,
  `product_ship_method` varchar(50) DEFAULT NULL,
  `product_shipping_price` varchar(10) DEFAULT NULL,
  `product_rank_index` int(10) DEFAULT NULL,
  `product_page_index` int(5) DEFAULT NULL,
  `product_promoted_status` varchar(3) DEFAULT NULL,
  `product_store_name` varchar(50) DEFAULT NULL,
  `product_store_url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;
