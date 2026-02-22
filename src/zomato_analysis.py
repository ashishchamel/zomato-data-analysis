{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "71092967-c7ce-4da7-b96c-834135bac168",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Files loaded\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "\n",
    "# Load Excel files\n",
    "\n",
    "food = pd.read_excel(r\"C:\\Users\\007bo\\OneDrive\\Desktop\\zomato\\food.xlsx\")\n",
    "orders = pd.read_excel(r\"C:\\Users\\007bo\\OneDrive\\Desktop\\zomato\\orders.xlsx\")\n",
    "restaurants = pd.read_excel(r\"C:\\Users\\007bo\\OneDrive\\Desktop\\zomato\\restaurant.xlsx\")\n",
    "users = pd.read_excel(r\"C:\\Users\\007bo\\OneDrive\\Desktop\\zomato\\users.xlsx\")\n",
    "\n",
    "print(\"Files loaded\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d60b2ea8-760a-4982-a50b-f481d764039c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Duplicates removed\n"
     ]
    }
   ],
   "source": [
    "# Remove duplicates\n",
    "\n",
    "food = food.drop_duplicates()\n",
    "orders = orders.drop_duplicates()\n",
    "restaurants = restaurants.drop_duplicates()\n",
    "users = users.drop_duplicates()\n",
    "\n",
    "print(\"Duplicates removed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "18cae9f3-d956-412d-9052-95ffecef4607",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Orders columns:\n",
      "Index(['order_date', 'sales_qty', 'sales_amount', 'currency', 'user_id',\n",
      "       'r_id', 'join_key'],\n",
      "      dtype='object')\n",
      "Restaurant columns:\n",
      "Index(['id', 'name', 'country', 'city', 'rating', 'rating_count', 'cuisine',\n",
      "       'link', 'address'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "# Standardize column names\n",
    "\n",
    "food.columns = food.columns.str.lower().str.replace(\" \", \"_\")\n",
    "orders.columns = orders.columns.str.lower().str.replace(\" \", \"_\")\n",
    "restaurants.columns = restaurants.columns.str.lower().str.replace(\" \", \"_\")\n",
    "users.columns = users.columns.str.lower().str.replace(\" \", \"_\")\n",
    "\n",
    "print(\"Orders columns:\")\n",
    "print(orders.columns)\n",
    "\n",
    "print(\"Restaurant columns:\")\n",
    "print(restaurants.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5f2465ec-db97-47b2-92e5-2a6caa8ca146",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Rename restaurant id\n",
    "\n",
    "restaurants.rename(columns={\"id\": \"r_id\"}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "61c45f2f-a767-410a-9851-90e90d101b9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After merging users: (150281, 12)\n",
      "After merging restaurants: (150281, 20)\n"
     ]
    }
   ],
   "source": [
    "# Merge datasets step by step\n",
    "\n",
    "df = orders.merge(users, on=\"user_id\", how=\"left\")\n",
    "print(\"After merging users:\", df.shape)\n",
    "\n",
    "df = df.merge(restaurants, on=\"r_id\", how=\"left\")\n",
    "print(\"After merging restaurants:\", df.shape)\n",
    "\n",
    "# Food table removed because orders have no food id relationship"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a1716ff6-af95-4126-bd13-c6a801b2e35c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  order_date  sales_qty  sales_amount currency  user_id      r_id  join_key  \\\n",
      "0 2017-10-10        100         41241      INR    49226  567335.0         1   \n",
      "1 2018-05-08          3            -1      INR    77359  531342.0         1   \n",
      "2 2018-04-06          1           875      INR     5321  158203.0         1   \n",
      "3 2018-04-11          1           583      INR    21343  187912.0         1   \n",
      "4 2018-06-18          6          7176      INR    75378  543530.0         1   \n",
      "\n",
      "               name_x  age gender marital_status      occupation  \\\n",
      "0       Teresa Garcia   27   Male        Married  Self Employeed   \n",
      "1         Dana Reeves   23   Male         Single         Student   \n",
      "2     Donald Anderson   24   Male        Married        Employee   \n",
      "3          Scott Cruz   22   Male         Single         Student   \n",
      "4  Heather Richardson   28   Male        Married        Employee   \n",
      "\n",
      "              name_y country    city rating     rating_count  \\\n",
      "0     AB FOODS POINT   India  Abohar     --  Too Few Ratings   \n",
      "1  Janta Sweet House   India  Abohar    4.4      50+ ratings   \n",
      "2  theka coffee desi   India  Abohar    3.8     100+ ratings   \n",
      "3          Singh Hut   India  Abohar    3.7      20+ ratings   \n",
      "4      GRILL MASTERS   India  Abohar     --  Too Few Ratings   \n",
      "\n",
      "                      cuisine  \\\n",
      "0            Beverages,Pizzas   \n",
      "1               Sweets,Bakery   \n",
      "2                   Beverages   \n",
      "3            Fast Food,Indian   \n",
      "4  Italian-American,Fast Food   \n",
      "\n",
      "                                                link  \\\n",
      "0  https://www.swiggy.com/restaurants/ab-foods-po...   \n",
      "1  https://www.swiggy.com/restaurants/janta-sweet...   \n",
      "2  https://www.swiggy.com/restaurants/theka-coffe...   \n",
      "3  https://www.swiggy.com/restaurants/singh-hut-n...   \n",
      "4  https://www.swiggy.com/restaurants/grill-maste...   \n",
      "\n",
      "                                             address  \n",
      "0  AB FOODS POINT, NEAR RISHI NARANG DENTAL CLINI...  \n",
      "1  Janta Sweet House, Bazar No.9, Circullar Road,...  \n",
      "2         theka coffee desi, sahtiya sadan road city  \n",
      "3    Singh Hut, CIRCULAR ROAD NEAR NEHRU PARK ABOHAR  \n",
      "4  GRILL MASTERS, ADA Heights, Abohar - Hanumanga...  \n"
     ]
    }
   ],
   "source": [
    "\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "048295fd-276c-4f3c-b5ac-907347fa4316",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After cleaning sales: (148670, 20)\n"
     ]
    }
   ],
   "source": [
    "# Clean sales_amount\n",
    "\n",
    "df[\"sales_amount\"] = pd.to_numeric(df[\"sales_amount\"], errors=\"coerce\")\n",
    "df = df[df[\"sales_amount\"].notna()]\n",
    "df = df[df[\"sales_amount\"] > 0]\n",
    "\n",
    "print(\"After cleaning sales:\", df.shape)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f883938f-4cd7-4a35-8834-ed4159b0afce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fix rating column\n",
    "\n",
    "df[\"rating\"] = pd.to_numeric(df[\"rating\"], errors=\"coerce\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "694d4b86-8b06-4c60-a899-914a817c94e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Rename duplicate name column\n",
    "\n",
    "df.rename(columns={\"name_x\": \"user_name\"}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "db3b42df-2ef8-4a67-8154-e3196599aa41",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Feature Engineering\n",
    "\n",
    "df[\"order_date\"] = pd.to_datetime(df[\"order_date\"])\n",
    "\n",
    "df[\"year\"] = df[\"order_date\"].dt.year\n",
    "df[\"month\"] = df[\"order_date\"].dt.month\n",
    "\n",
    "df[\"sales_qty\"] = pd.to_numeric(df[\"sales_qty\"], errors=\"coerce\")\n",
    "\n",
    "df[\"cost_per_item\"] = df[\"sales_amount\"] / df[\"sales_qty\"]\n",
    "df[\"cost_per_item\"] = df[\"cost_per_item\"].replace([float(\"inf\"), -float(\"inf\")], None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6166c68b-50aa-47c9-84ac-c4a404437597",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Rating buckets\n",
    "\n",
    "df[\"rating_bucket\"] = pd.cut(\n",
    "    df[\"rating\"],\n",
    "    bins=[0, 2, 3, 4, 5],\n",
    "    labels=[\"Poor\", \"Average\", \"Good\", \"Excellent\"]\n",
    ")\n",
    "\n",
    "df[\"rating_bucket\"] = df[\"rating_bucket\"].cat.add_categories(\"Unknown\")\n",
    "df[\"rating_bucket\"] = df[\"rating_bucket\"].fillna(\"Unknown\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "91c84257-8525-4f7a-9e0a-94d87d1a3e8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feature engineering done\n"
     ]
    }
   ],
   "source": [
    "# Price segments\n",
    "\n",
    "df[\"price_segment\"] = pd.qcut(df[\"sales_amount\"], 3,\n",
    "                              labels=[\"Budget\", \"Mid\", \"Premium\"])\n",
    "\n",
    "print(\"Feature engineering done\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "001f16e8-28df-443a-81bc-8cd1a30c7c81",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(148670, 25)\n",
      "       sales_amount  cost_per_item        rating\n",
      "count  1.486700e+05  148670.000000  60874.000000\n",
      "mean   6.635939e+03     462.857313      3.894975\n",
      "std    3.007124e+04     549.833360      0.459718\n",
      "min    5.000000e+00       0.902439      1.000000\n",
      "25%    1.760000e+02     130.000000      3.700000\n",
      "50%    5.190000e+02     254.666667      4.000000\n",
      "75%    3.065000e+03     544.666667      4.200000\n",
      "max    1.510944e+06    5056.000000      5.000000\n",
      "price_segment\n",
      "Budget     50196\n",
      "Premium    49522\n",
      "Mid        48952\n",
      "Name: count, dtype: int64\n",
      "rating_bucket\n",
      "Unknown      87796\n",
      "Good         33184\n",
      "Excellent    24555\n",
      "Average       2929\n",
      "Poor           206\n",
      "Name: count, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Quick checks\n",
    "\n",
    "\n",
    "print(df.shape)\n",
    "\n",
    "print(df[[\"sales_amount\", \"cost_per_item\", \"rating\"]].describe())\n",
    "\n",
    "print(df[\"price_segment\"].value_counts())\n",
    "print(df[\"rating_bucket\"].value_counts())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "13b8223b-2c4c-4ce2-aa48-2e586c48ac4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\007bo\\AppData\\Local\\Temp\\ipykernel_12604\\2539811607.py:7: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.\n",
      "  df.groupby(\"rating_bucket\")[\"sales_amount\"].sum()\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "cuisine\n",
       "North Indian,Chinese    44956268\n",
       "Indian                  42626090\n",
       "North Indian            33670996\n",
       "Chinese                 27259296\n",
       "Indian,Chinese          25738592\n",
       "South Indian            21944967\n",
       "Bakery                  19052451\n",
       "Pizzas                  16546168\n",
       "Beverages               14479459\n",
       "Bakery,Desserts         14430826\n",
       "Name: sales_amount, dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Basic EDA for Tableau\n",
    "\n",
    "df.groupby(\"year\")[\"sales_amount\"].sum()\n",
    "\n",
    "df.groupby(\"city\")[\"sales_amount\"].sum().sort_values(ascending=False).head(10)\n",
    "\n",
    "df.groupby(\"rating_bucket\")[\"sales_amount\"].sum()\n",
    "\n",
    "df.groupby(\"cuisine\")[\"sales_amount\"].sum().sort_values(ascending=False).head(10)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "9e86f03b-6f8a-4556-8949-e82f3e9c046e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DONE - Tableau file created\n"
     ]
    }
   ],
   "source": [
    "# Export final dataset\n",
    "# =========================\n",
    "\n",
    "df.to_excel(r\"C:\\Users\\007bo\\OneDrive\\Desktop\\zomato\\zomato_tableau_ready.xlsx\", index=False)\n",
    "\n",
    "print(\"DONE - Tableau file created\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c2d01f7-e40a-466d-aea0-f2ea93a8d84f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
