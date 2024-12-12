import { Routes } from '@angular/router';
import {AccueilComponent} from "./features/accueil/page/accueil/accueil.component";
import {TravelListeComponent} from "./features/travel/page/travel-liste/travel-liste.component";

export const routes: Routes = [
  {path: "accueil", component: AccueilComponent},
  {path: "resultats", component: TravelListeComponent},
];
