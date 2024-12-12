import { Routes } from '@angular/router';
import {AccueilComponent} from "./features/accueil/page/accueil/accueil.component";

export const routes: Routes = [
  {path: "accueil", component: AccueilComponent},
  { path: "", redirectTo: "accueil", pathMatch: "full" },
];
